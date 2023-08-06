
from types import SimpleNamespace

from django.apps import apps
from django.utils.translation import gettext_lazy as _
from django.apps import AppConfig

__all__ = ['get_app_label', 'DraftailMathsConfig']


class DraftailMathsConfig(AppConfig):

    name = 'draftail_maths'
    label = 'draftail_maths'
    verbose_name = _("Query Kit")
    default_auto_field = 'django.db.models.BigAutoField'
    app_settings_getters = SimpleNamespace()

    def import_models(self):

        from django_auxiliaries.app_settings import configure

        self.app_settings_getters = configure(self)

        super().import_models()


def get_app_label():
    return DraftailMathsConfig.label


def get_app_config():
    return apps.get_app_config(DraftailMathsConfig.label)
