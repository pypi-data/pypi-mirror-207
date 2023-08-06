from django.urls import reverse
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class WagtailRicherTextConfig(AppConfig):
    name = 'wagtail_richer_text'
    label = 'wagtail_richer_text'
    verbose_name = _("Wagtail Richer Text")
    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):
        pass


def get_app_label():
    return WagtailRicherTextConfig.label


def reverse_app_url(identifier):
    return reverse(f'{WagtailRicherTextConfig.label}:{identifier}')

