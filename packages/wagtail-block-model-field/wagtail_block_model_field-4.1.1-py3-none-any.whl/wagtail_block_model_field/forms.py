from wagtail.blocks import BlockField

__all__ = ['BlockModelFormField']


class BlockModelFormField(BlockField):

    def __init__(self, *args, **kwargs):
        super(BlockModelFormField, self).__init__(*args, **kwargs)

    def clean(self, value):
        return self.block.clean(value)

    def has_changed(self, initial_value, data_value):
        return self.block.get_prep_value(initial_value) != self.block.get_prep_value(data_value)
