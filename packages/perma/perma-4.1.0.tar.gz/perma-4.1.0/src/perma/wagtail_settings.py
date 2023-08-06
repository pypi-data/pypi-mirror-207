from django.db import models as django_models
from wagtail.admin.panels import FieldPanel
from wagtail.contrib.settings.models import (
    BaseGenericSetting,
    BaseSiteSetting,
    register_setting,
)

from .apps import get_app_label

APP_LABEL = get_app_label()


@register_setting
class PermaSiteSettings(BaseSiteSetting):

    canonical_record_index_page = django_models.ForeignKey(APP_LABEL + '.recordindexpage',
                                                            null=True, blank=True, related_name='+',
                                                            on_delete=django_models.SET_NULL)
    panels = [
            FieldPanel('canonical_record_index_page'),
        ]
