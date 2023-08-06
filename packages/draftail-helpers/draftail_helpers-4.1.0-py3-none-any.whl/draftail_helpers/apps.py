from django.urls import reverse
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DraftailHelpersConfig(AppConfig):
    name = 'draftail_helpers'
    label = 'draftail_helpers'
    verbose_name = _("Draftail Helpers")
    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):
        pass


def get_app_label():
    return DraftailHelpersConfig.label


def reverse_app_url(identifier):
    return reverse(f'{DraftailHelpersConfig.label}:{identifier}')

