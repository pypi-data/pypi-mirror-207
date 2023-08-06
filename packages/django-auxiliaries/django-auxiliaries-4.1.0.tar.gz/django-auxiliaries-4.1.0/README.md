django-auxiliaries
==================

A diverse collection of methods, classes and modules we find useful when developing for Django (and Wagtail). Please bear with us while we prepare more detailed documentation.

Compatibility
-------------

`django-auxiliaries`' major.minor version number indicates the Django release it is compatible with. Currently this is Django 4.1.

Installation
------------

1. Install using `pip`:
  ```shell
  pip install django-auxiliaries
  ```
2. If you use functional that requires an app (such as tags), add
   `django_auxiliaries` to your `INSTALLED_APPS` setting:
   ```python
   INSTALLED_APPS = [
     # ...
     'django_auxiliaries'
     # ...
   ]
   ```
