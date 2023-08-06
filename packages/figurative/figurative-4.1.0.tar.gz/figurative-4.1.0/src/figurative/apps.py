
import sys
from django.conf import settings
from django.db import DEFAULT_DB_ALIAS
from django.urls import reverse
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


def is_running_without_database():
    engine = settings.DATABASES[DEFAULT_DB_ALIAS]['ENGINE']
    return engine == 'django.db.backends.dummy'


class FigurativeConfig(AppConfig):
    name = 'figurative'
    label = 'figurative'
    verbose_name = _("Figurative")
    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):

        if is_running_without_database() or "makemigrations" in sys.argv or "migrate" in sys.argv:
            return


def get_app_label():
    return FigurativeConfig.label


def reverse_app_url(identifier):
    return reverse(f'{FigurativeConfig.label}:{identifier}')

