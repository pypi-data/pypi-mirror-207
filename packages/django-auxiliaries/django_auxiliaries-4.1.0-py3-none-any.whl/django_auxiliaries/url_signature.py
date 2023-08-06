
import base64
import hashlib
import hmac

from django.conf import settings
from django.utils.encoding import force_str
from django.urls import reverse

from .apps import get_app_label

__all__ = ['generate_signature', 'verify_signature', 'generate_signed_url', 'verify_signed_url']

APP_LABEL = get_app_label()

DEFAULT_KEY_SETTING = 'SECRET_KEY'


def generate_signature(url, key=None, key_setting=DEFAULT_KEY_SETTING):
    if key is None:
        key = getattr(settings, key_setting)

    # Key must be a bytes object
    if isinstance(key, str):
        key = key.encode()

    # Based on libthumbor hmac generation
    # https://github.com/thumbor/libthumbor/blob/b19dc58cf84787e08c8e397ab322e86268bb4345/libthumbor/crypto.py#L50
    return force_str(base64.urlsafe_b64encode(hmac.new(key, url.encode(), hashlib.sha1).digest()))


def verify_signature(signature, url, key=None, key_setting=DEFAULT_KEY_SETTING):
    return force_str(signature) == generate_signature(url, key=key, key_setting=key_setting)


def generate_signed_url(*args, url_specifier, key=None, key_setting=DEFAULT_KEY_SETTING):
    url = reverse(url_specifier, args=args)
    signature = generate_signature(url, key=key, key_setting=key_setting)
    url = reverse(url_specifier, args=list(args) + [signature + "/"])  # Always add trailing forward slash
    return url


def verify_signed_url(*args, signature, url_specifier, key=None, key_setting=DEFAULT_KEY_SETTING):
    url = reverse(url_specifier, args=args)

    if signature.endswith("/"):
        signature = signature[:-1]

    return verify_signature(signature.encode(), url, key=key, key_setting=key_setting)
