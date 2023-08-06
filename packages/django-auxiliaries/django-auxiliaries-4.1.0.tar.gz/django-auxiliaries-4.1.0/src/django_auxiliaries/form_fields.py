
from django.forms.fields import Field, CharField
from django.forms.widgets import MultipleHiddenInput, HiddenInput
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

__all__ = ['ListField', 'StaticFormField']


class ListField(Field):

    hidden_widget = MultipleHiddenInput
    widget = MultipleHiddenInput
    default_error_messages = {
        "invalid_element": _(
            "An element has the format identifier.identifier:key. %(value)s is not in a valid format."
        ),
        "invalid_list": _("Enter a list of values."),
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __deepcopy__(self, memo):
        result = super().__deepcopy__(memo)
        # result.some_field = copy.deepcopy(self.some_field, memo)
        return result

    def to_python(self, value):
        if value in self.empty_values:
            return []
        elif not isinstance(value, (list, tuple)):
            raise ValidationError(
                self.error_messages["invalid_list"], code="invalid_list"
            )
        return [str(val) for val in value]

    def validate(self, value):
        """Validate that the input is a list or tuple."""
        if self.required and not value:
            raise ValidationError(self.error_messages["required"], code="required")
        # Validate that each element in the value list has a valid format.
        for val in value:
            if not self.is_valid_element_value(val):
                raise ValidationError(
                    self.error_messages["invalid_element"],
                    code="invalid_element",
                    params={"value": val},
                )

    # noinspection PyMethodMayBeStatic
    def is_valid_element_value(self, value):
        return isinstance(value, str)

    def has_changed(self, initial, data):
        if self.disabled:
            return False
        if initial is None:
            initial = []
        if data is None:
            data = []
        if len(initial) != len(data):
            return True
        initial_set = {str(value) for value in initial}
        data_set = {str(value) for value in data}
        return data_set != initial_set


class StaticFormField(CharField):

    def __init__(self, *args, **kwargs):
        kwargs['widget'] = HiddenInput
        super().__init__(*args, **kwargs)

    def bound_data(self, data, initial):
        return ''

    def has_changed(self, initial, data):
        return True
