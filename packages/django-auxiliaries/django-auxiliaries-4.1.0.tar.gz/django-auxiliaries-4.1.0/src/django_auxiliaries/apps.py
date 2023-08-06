
import sys
from django.conf import settings
from django.db import DEFAULT_DB_ALIAS
from django.urls import reverse
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


def is_running_without_database():
    engine = settings.DATABASES[DEFAULT_DB_ALIAS]['ENGINE']
    return engine == 'django.db.backends.dummy'


class DjangoAuxiliariesConfig(AppConfig):
    name = 'django_auxiliaries'
    label = 'django_auxiliaries'
    verbose_name = _("Django Auxiliaries")
    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):

        if is_running_without_database() or "makemigrations" in sys.argv or "migrate" in sys.argv:
            return

        from .templatetags.django_auxiliaries_tags import map_modules_to_app_labels, discover_installed_support_tags

        map_modules_to_app_labels()
        discover_installed_support_tags()

def get_app_label():
    return DjangoAuxiliariesConfig.label


def reverse_app_url(identifier):
    return reverse(f'{DjangoAuxiliariesConfig.label}:{identifier}')

