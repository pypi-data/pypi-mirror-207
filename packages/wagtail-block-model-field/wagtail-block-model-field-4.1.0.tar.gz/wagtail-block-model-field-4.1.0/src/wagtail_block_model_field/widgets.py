import json
from django import forms
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.utils.functional import cached_property

from wagtail.core.blocks import BlockWidget

from django_auxiliaries.templatetags.django_auxiliaries_tags import tagged_static

from .apps import get_app_label

__all__ = ['BlockModelWidget']


class BlockModelWidget(BlockWidget):
    """Wraps a block object as a widget so that it can be incorporated into a Django form"""

    def __init__(self, block_def, attrs=None):
        super().__init__(block_def, attrs=attrs)

    def value_from_datadict(self, data, files, name):
        return self.block_def.value_from_datadict(data, files, name)

    def modify_html(self, name, fragment):
        fragment = fragment.replace('<script>', '<script id="{}">'.format(name + "-script"))
        fragment = fragment.replace('initBlockWidget', 'initBlockModelWidget')
        fragment = mark_safe(fragment)
        return fragment

    def render(self, name, value, attrs=None, renderer=None):
        fragment = super(BlockModelWidget, self).render(name, value, attrs=attrs, renderer=renderer)
        fragment = self.modify_html(name, fragment)
        return fragment

    def render_with_errors(self, name, value, attrs=None, errors=None, renderer=None):
        fragment = super().render_with_errors(name, value, attrs=attrs, errors=errors, renderer=renderer)
        fragment = self.modify_html(name, fragment)
        return fragment

    @cached_property
    def media(self):

        result = super().media + forms.Media(
            js=[
                tagged_static(get_app_label() + '/js/block_model_field_widget.js'),
            ],
            css=[
            ]
        )

        return result
