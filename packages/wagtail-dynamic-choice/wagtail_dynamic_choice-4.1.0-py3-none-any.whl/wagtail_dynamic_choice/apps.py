from django.urls import reverse
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class WagtailDynamicChoiceConfig(AppConfig):
    name = 'wagtail_dynamic_choice'
    label = 'wagtail_dynamic_choice'
    verbose_name = _("Wagtail Dynamic Choice")
    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):
        pass


def get_app_label():
    return WagtailDynamicChoiceConfig.label


def reverse_app_url(identifier):
    return reverse(f'{WagtailDynamicChoiceConfig.label}:{identifier}')

