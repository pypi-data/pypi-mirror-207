from django.db import models
from django import forms

from .form_fields import StaticFormField

__all__ = ['AutoDeleteFileField', 'MultipleChoiceField', 'StaticField']


class RobustFieldFile(models.FileField.attr_class):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, name, content, save=True):
        generated_name = self.field.generate_filename(self.instance, name)
        provisional_name = self.storage.get_available_name(generated_name, max_length=self.field.max_length)

        if provisional_name != generated_name and self.storage.exists(generated_name):
            self.storage.delete(generated_name)

        super().save(name, content, save)


class AutoDeleteFileField(models.FileField):

    attr_class = RobustFieldFile

    """
    A file field that clears a previous file from storage if requested in the form.
    """

    def __init__(self, verbose_name=None, name=None, **kwargs):
        super().__init__(verbose_name, name, **kwargs)

    def save_form_data(self, instance, data):

        if data is not None and not data:
            # False-ish value that is not None means clear file
            file = getattr(instance, self.attname)
            file.delete(save=False)

        super().save_form_data(instance, data)


class MultipleChoiceField(models.CharField):

    def formfield(self, **kwargs):
        # As with CharField, this will cause URL validation to be performed
        # twice.
        defaults = {
            'form_class': forms.MultipleChoiceField,
        }
        defaults.update(kwargs)
        return super().formfield(**defaults)


class StaticField(models.CharField):

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 20
        kwargs['default'] = ''
        kwargs['blank'] = True
        kwargs['null'] = True
        kwargs['name'] = ''
        kwargs['verbose_name'] = ''
        super().__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        return super().formfield(
            **{
                "form_class": StaticFormField,
                **kwargs,
            }
        )
