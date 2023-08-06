# -*- coding: utf-8 -*-

import sys
from django.conf import settings
from django.db import DEFAULT_DB_ALIAS
from django.urls import reverse
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


def is_running_without_database():
    engine = settings.DATABASES[DEFAULT_DB_ALIAS]['ENGINE']
    return engine == 'django.db.backends.dummy'


class StreetwiseConfig(AppConfig):
    name = 'streetwise'
    label = 'streetwise'
    verbose_name = _("Streetwise")
    default_auto_field = 'django.db.models.BigAutoField'

    def import_models(self):

        from django_auxiliaries.app_settings import configure

        configure(self)

        from django_auxiliaries.variable_scope import register_variable_scope

        register_variable_scope(self.label, map_view_index=0)

        super().import_models()

    def ready(self):

        if is_running_without_database() or "makemigrations" in sys.argv or "migrate" in sys.argv:
            return


def get_app_label():
    return StreetwiseConfig.label


def reverse_app_url(identifier):
    return reverse(f'{StreetwiseConfig.label}:{identifier}')

