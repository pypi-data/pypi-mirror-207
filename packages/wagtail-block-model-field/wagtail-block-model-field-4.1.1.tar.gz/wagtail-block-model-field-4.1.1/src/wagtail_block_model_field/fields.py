import json
import datetime

from django.db.models import Field
from django.core.serializers.json import DjangoJSONEncoder
from django.core.exceptions import ImproperlyConfigured
from django.utils.safestring import SafeString

from wagtail import blocks
from wagtail.rich_text import RichText
from wagtail.admin.panels import FieldPanel
from wagtail.admin import compare

from .widgets import *
from .forms import BlockModelFormField

__all__ = ['BlockModelField', 'BlockModelFieldComparison']


class BlockModelFieldComparison(compare.RichTextFieldComparison):
    pass


class ModelProperty:

    def __init__(self, field):
        self.field = field

    def __get__(self, obj, type=None):
        if obj is None:
            return self
            
        if self.field.name not in obj.__dict__:
            obj.refresh_from_db(fields=[self.field.name])
            
        value = obj.__dict__[self.field.name]

        return value

    def __set__(self, obj, value):
        obj.__dict__[self.field.name] = self.field.to_python(value)


class BlockModelField(Field):

    BlockModelFieldProperty = ModelProperty

    @property
    def block_def(self):
        return self.block_

    def __init__(self, block, value_class=None, **kwargs):

        # if 'default' not in kwargs:
        #    kwargs['default'] = block.get_default()  # block.get_prep_value(block.get_default())

        is_auto_value_class = False

        if value_class is None:

            is_auto_value_class = True

            if isinstance(block, blocks.StructBlock):
                value_class = blocks.StructValue
            elif isinstance(block, blocks.StreamBlock):
                value_class = blocks.StreamValue
            elif isinstance(block, blocks.CharBlock):
                value_class = str
            elif isinstance(block, blocks.TextBlock):
                value_class = str
            elif isinstance(block, blocks.FloatBlock):
                value_class = float
            elif isinstance(block, blocks.DecimalBlock):
                value_class = int
            elif isinstance(block, blocks.IntegerBlock):
                value_class = int
            elif isinstance(block, blocks.RegexBlock):
                value_class = str
            elif isinstance(block, blocks.URLBlock):
                value_class = str
            elif isinstance(block, blocks.BooleanBlock):
                value_class = bool
            elif isinstance(block, blocks.DateBlock):
                value_class = datetime.date
            elif isinstance(block, blocks.TimeBlock):
                value_class = datetime.time
            elif isinstance(block, blocks.DateTimeBlock):
                value_class = datetime.datetime
            elif isinstance(block, blocks.EmailBlock):
                value_class = str
            elif isinstance(block, blocks.ChoiceBlock):
                value_class = str
            elif isinstance(block, blocks.MultipleChoiceBlock):
                value_class = list
            elif isinstance(block, blocks.RichTextBlock):
                value_class = RichText
            elif isinstance(block, blocks.RawHTMLBlock):
                value_class = SafeString
            elif isinstance(block, blocks.ChooserBlock):
                value_class = int
            else:
                raise ImproperlyConfigured(('BlockModelField could not identify the value class ' +
                                            'of the given block of type \'{}\'').format(type(block)))

        if issubclass(value_class, str):
            raise ImproperlyConfigured(('BlockModelField does not support str as a value class. If' +
                                        'the given block of type \'{}\' requires a str value class, ' +
                                        'it cannot be used with BlockModelField.').format(type(block)))

        kwargs['blank'] = not block.required
        kwargs['null'] = not block.required

        super().__init__(**kwargs)

        svd_get_prep_value = block.get_prep_value
        svd_get_form_state = block.get_form_state

        def get_prep_value(value):
            if not value:
                value = self.get_default()

            return svd_get_prep_value(value)

        def get_form_state(value):
            if not value:
                value = self.get_default()

            return svd_get_form_state(value)

        block.get_prep_value = get_prep_value
        block.get_form_state = get_form_state
        self.block_ = block
        self.value_class_ = value_class
        self.is_auto_value_class_ = is_auto_value_class

    def get_internal_type(self):
        """ Indicate the database value type indirectly, by referencing an existing Django field. """
        return 'TextField'

    def get_panel(self):
        return FieldPanel

    def deconstruct(self):
        name, path, _, kwargs = super().deconstruct()

        args = [self.block_]

        if not self.is_auto_value_class_:
            args.append(self.value_class_)

        if 'blank' in kwargs:
            del kwargs['blank']

        if 'null' in kwargs:
            del kwargs['null']

        return name, path, args, kwargs

    def get_default(self):
        return self.block_.get_default()

    def clean(self, value, model_instance):
        """
        Convert the value's type and run validation. Validation errors
        from to_python() and validate() are propagated. Return the correct
        value if no error is raised.
        """
        value = self.to_python(value)
        self.validate(value, model_instance)
        self.run_validators(value)
        return value

    def from_db_value(self, value, expression, connection, context=None):
        """
        Always return model type!

        If your custom Field class deals with data structures that are more complex than strings, dates, integers, or
        floats, then you may need to override from_db_value() and to_python().

        If present for the field subclass, from_db_value() will be called in all circumstances when the data is loaded
        from the database, including in aggregates and values() calls.
        """

        # if isinstance(value, str) and value:

        try:
            value = json.loads(value)
        except ValueError as error:
            raise error

        return self._to_python(value)

    def get_prep_value(self, value):
        """
            Perform preliminary non-db specific value checks and conversions to be used as query values for the
            database backend.

            The value returned by this method should always be compatible to the database value type.
        """

        value = self.block_.get_prep_value(value)
        return value

    def _to_python(self, value):

        try:
            value = self.block_.to_python(value)
        except Exception as error:

            # is this a serialised value created by value_to_string()?

            if not isinstance(value, str) or not value:
                raise error

            try:
                value = json.loads(value)
            except:
                raise error

            value = self.block_.to_python(value)

        return value

    def to_python(self, value):
        """
        Always return model type!

        to_python() is called by deserialization and during the clean() method used from forms.

        As a general rule, to_python() should deal gracefully with any of the following arguments:
            An instance of the correct type (e.g., Hand in our ongoing example).
            A string. If it is a string, it might have been produced by value_to_string()
            None (if the field allows null=True)
        """

        if not value:
            return self.get_default()

        if isinstance(value, self.value_class_):
            return value

        value = self._to_python(value)
        return value

    def get_db_prep_value(self, value, connection, prepared=False):
        """
        Return field's value prepared for interacting with the database backend.
        """
        prep_value = super().get_db_prep_value(value, connection, prepared)
        prep_value = json.dumps(prep_value, cls=DjangoJSONEncoder)
        return prep_value

    def get_db_prep_save(self, value, connection):
        """Return field's value prepared for saving into a database."""
        prep_value = super().get_db_prep_save(value, connection)
        return prep_value

    def formfield(self, **kwargs):
        """
        Override formfield to use a plain forms.Field so that we do no transformation on the value
        (as distinct from the usual fallback of forms.CharField, which transforms it into a string).
        """
        defaults = {'form_class': BlockModelFormField, 'block': self.block_, 'widget': BlockModelWidget(self.block_)}
        defaults.update(kwargs)
        return super().formfield(**defaults)

    def value_to_string(self, obj):
        """
        This is used for serialization.
        """
        value = self.value_from_object(obj)
        value = self.get_prep_value(value)
        value = json.dumps(value, cls=DjangoJSONEncoder)
        return value

    def get_searchable_content(self, value):
        return self.block_.get_searchable_content(value)

    def check(self, **kwargs):
        errors = super().check(**kwargs)
        errors.extend(self.block_.check(field=self, **kwargs))
        return errors

    def contribute_to_class(self, cls, name, **kwargs):
        super().contribute_to_class(cls, name, **kwargs)

        # Add ModelProperty descriptor to allow the field to be set from a list or a
        # JSON string.
        setattr(cls, self.name, self.BlockModelFieldProperty(self))

