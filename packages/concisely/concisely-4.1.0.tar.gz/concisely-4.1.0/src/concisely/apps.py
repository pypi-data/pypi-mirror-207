from django.urls import reverse
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ConciselyConfig(AppConfig):
    name = 'concisely'
    label = 'concisely'
    verbose_name = _("Concisely")
    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):
        pass


def get_app_label():
    return ConciselyConfig.label


def reverse_app_url(identifier):
    return reverse(f'{ConciselyConfig.label}:{identifier}')

