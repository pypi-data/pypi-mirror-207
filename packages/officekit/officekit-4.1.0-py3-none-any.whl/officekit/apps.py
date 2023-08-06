
from types import SimpleNamespace

from django.apps import apps
from django.urls import reverse
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class OfficekitConfig(AppConfig):
    name = 'officekit'
    label = 'officekit'
    verbose_name = _("Office Kit")
    default_auto_field = 'django.db.models.BigAutoField'
    app_settings_getters = SimpleNamespace()

    def import_models(self):

        from django_auxiliaries.app_settings import configure

        self.app_settings_getters = configure(self)

        super().import_models()

    def ready(self):
        pass


def get_app_label():
    return OfficekitConfig.label


def reverse_app_url(identifier):
    return reverse(f'{OfficekitConfig.label}:{identifier}')


def get_app_config():
    return apps.get_app_config(OfficekitConfig.label)
