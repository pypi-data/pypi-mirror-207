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


class AdedeConfig(AppConfig):
    name = 'adede'
    label = 'adede'
    verbose_name = _("Adede")
    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):

        if is_running_without_database() or "makemigrations" in sys.argv or "migrate" in sys.argv:
            return


def get_app_label():
    return AdedeConfig.label


def reverse_app_url(identifier):
    return reverse(f'{AdedeConfig.label}:{identifier}')

