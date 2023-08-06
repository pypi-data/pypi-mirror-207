from django.forms import Field
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

from .widgets import DynamicChoiceWidget
from .function_specifier import FunctionSpecifier

__all__ = ['DynamicChoiceField']


class DynamicChoiceField(Field):

    widget = DynamicChoiceWidget
    default_error_messages = {
        "invalid_choice": _(
            "Select a valid choice. %(value)s is not one of the available choices."
        ),
    }

    def __init__(self, *, choices_function_name, **kwargs):
        super().__init__(**kwargs)
        self.choices_function = FunctionSpecifier(function_path=choices_function_name)

    def to_python(self, value):
        """Return a string."""
        if value in self.empty_values:
            return ""
        return str(value)

    def validate(self, value):
        """Validate that the input is in self.choices."""
        super().validate(value)
        if value and not self.valid_value(value):
            raise ValidationError(
                self.error_messages["invalid_choice"],
                code="invalid_choice",
                params={"value": value},
            )

    def valid_value(self, value):
        """Check to see if the provided value is a valid choice."""
        text_value = str(value)
        for k, v in self.choices_function():
            if isinstance(v, (list, tuple)):
                # This is an optgroup, so look inside the group for options
                for k2, v2 in v:
                    if value == k2 or text_value == str(k2):
                        return True
            else:
                if value == k or text_value == str(k):
                    return True
        return False

