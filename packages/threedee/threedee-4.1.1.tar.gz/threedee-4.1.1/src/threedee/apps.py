# -*- coding: utf-8 -*-
from types import SimpleNamespace
import sys
from django.conf import settings
from django.db import DEFAULT_DB_ALIAS
from django.urls import reverse
from django.apps import AppConfig
from django.apps import apps
from django.utils.translation import gettext_lazy as _


def is_running_without_database():
    engine = settings.DATABASES[DEFAULT_DB_ALIAS]['ENGINE']
    return engine == 'django.db.backends.dummy'


# noinspection SpellCheckingInspection
class ThreeDeeConfig(AppConfig):
    # noinspection SpellCheckingInspection
    name = 'threedee'

    # noinspection SpellCheckingInspection
    label = 'threedee'

    # noinspection SpellCheckingInspection
    verbose_name = _("Threedee")
    default_auto_field = 'django.db.models.BigAutoField'
    app_settings_getters = SimpleNamespace()

    def import_models(self):

        from django_auxiliaries.app_settings import configure

        self.app_settings_getters = configure(self)

        super().import_models()

    def ready(self):

        # noinspection SpellCheckingInspection
        if is_running_without_database() or "makemigrations" in sys.argv or "migrate" in sys.argv:
            return


def get_app_label():
    return ThreeDeeConfig.label


def reverse_app_url(identifier):
    return reverse(f'{ThreeDeeConfig.label}:{identifier}')


def get_app_config():
    return apps.get_app_config(ThreeDeeConfig.label)
