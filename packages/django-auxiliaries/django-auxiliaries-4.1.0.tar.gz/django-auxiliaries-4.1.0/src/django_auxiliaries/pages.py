from django.apps import apps as django_apps
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

__all__ = ['get_site_page_model']


def get_site_page_model():
    """
    Return the site page model that is active in this project.
    """
    try:
        return django_apps.get_model(settings.SITE_PAGE_MODEL, require_ready=False)
    except ValueError:
        raise ImproperlyConfigured("SITE_PAGE_MODEL must be of the form 'app_label.model_name'")
    except LookupError:
        raise ImproperlyConfigured(
            "SITE_PAGE_MODEL refers to model '%s' that has not been installed" % settings.SITE_PAGE_MODEL
        )

