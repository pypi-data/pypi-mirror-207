# -*- coding: utf-8 -*-

import sys

from django.conf import settings
from django.db import DEFAULT_DB_ALIAS
from django.apps import AppConfig
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


def is_running_without_database():
    engine = settings.DATABASES[DEFAULT_DB_ALIAS]['ENGINE']
    return engine == 'django.db.backends.dummy'


class WagtailDynamicStreamBlockConfig(AppConfig):
    name = 'wagtail_dynamic_stream_block'
    label = 'wagtail_dynamic_stream_block'
    verbose_name = _("Wagtail Dynamic Stream Block")
    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):

        if is_running_without_database() or "makemigrations" in sys.argv or "migrate" in sys.argv:
            return

        from .blocks import update_dynamic_stream_blocks

        update_dynamic_stream_blocks()


def get_app_label():
    return WagtailDynamicStreamBlockConfig.label


def reverse_app_url(identifier):
    return reverse(f'{WagtailDynamicStreamBlockConfig.label}:{identifier}')
