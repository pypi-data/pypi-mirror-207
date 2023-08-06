
from django.core.validators import RegexValidator

__all__ = ['python_identifier_validator', 'css_compatible_identifier_validator']


python_identifier_validator = \
    RegexValidator(
       '^[A-Za-z_][A-Za-z_0-9]*$',
       code='invalid_identifier',
       message='A valid identifier starts with an alphanumeric letter or underscore and contains '
               'only alphanumeric letters, underscores or digits.')


css_compatible_identifier_validator = \
    RegexValidator(
       '^[A-Za-z_][A-Za-z_0-9-]*$',
       code='invalid_identifier',
       message='A valid identifier starts with an alphanumeric letter or underscore and contains '
               'only alphanumeric letters, underscores, digits or hyphens.')
