from types import SimpleNamespace
import importlib

from django.conf import settings

__all__ = ['configure']


def configure(app_config):

    result = SimpleNamespace()

    try:
        app_settings = importlib.import_module(app_config.name + ".default_settings")

        for key, value in app_settings.__dict__.items():

            if key.startswith('_'):
                continue

            def retrieve_app_setting():
                return getattr(settings, key)

            setattr(result, key.lower(), retrieve_app_setting)

            if hasattr(settings, key):
                continue

            setattr(settings, key, value)

    except (ModuleNotFoundError, ImportError):
        pass

    return result
