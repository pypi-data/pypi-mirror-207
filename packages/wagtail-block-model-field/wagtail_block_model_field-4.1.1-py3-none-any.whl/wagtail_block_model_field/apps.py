# -*- coding: utf-8 -*-

from django.apps import AppConfig
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class WagtailBlockModelFieldConfig(AppConfig):
    name = 'wagtail_block_model_field'
    label = 'wagtail_block_model_field'
    verbose_name = _("Wagtail Block Model Field")
    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):

        from wagtail.admin.compare import register_comparison_class
        from .fields import BlockModelField, BlockModelFieldComparison

        register_comparison_class(BlockModelField, comparison_class=BlockModelFieldComparison)


def get_app_label():
    return WagtailBlockModelFieldConfig.label


def reverse_app_url(identifier):
    return reverse(f'{WagtailBlockModelFieldConfig.label}:{identifier}')
