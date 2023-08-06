
from django.db.models.fields import CharField
from django.db.models.fields.json import JSONField

from django import forms

from .function_specifier import FunctionSpecifier

__all__ = ['DynamicChoiceField', 'DynamicMultipleChoiceField']


class DynamicChoiceField(CharField):

    form_class = forms.TypedChoiceField

    def __init__(self, *args, choices_function_name, **kwargs):
        super().__init__(*args, **kwargs)
        self.choices_function = FunctionSpecifier(function_path=choices_function_name)

    def formfield(self, **kwargs):

        if self.choices_function is not None:

            choices = self.choices_function()

            # include_blank = not (self.has_default() or "initial" in kwargs)
            # defaults = {"choices": self.get_choices(include_blank=include_blank)}

            # Many of the subclass-specific formfield arguments (min_value,
            # max_value) don't apply for choice fields, so be sure to only pass
            # the values that TypedChoiceField will understand.

            for k in list(kwargs):
                if k not in (
                        "coerce",
                        "empty_value",
                        "choices",
                        "required",
                        "widget",
                        "label",
                        "initial",
                        "help_text",
                        "error_messages",
                        "show_hidden_initial",
                        "disabled",
                        "max_length"
                ):
                    del kwargs[k]

            kwargs.update({
                'form_class': self.form_class,
                'choices': choices,
                'coerce': self.to_python
            })

        return super(CharField, self).formfield(**kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()

        kwargs['choices_function_name'] = self.choices_function.function_path

        return name, path, args, kwargs


class DynamicMultipleChoiceField(JSONField):

    form_class = forms.TypedMultipleChoiceField

    def __init__(self, *args, choices_function_name, default, **kwargs):
        super().__init__(*args, default=default, **kwargs)
        self.choices_function = FunctionSpecifier(function_path=choices_function_name)

    def formfield(self, **kwargs):

        if self.choices_function is not None:

            choices = self.choices_function()

            # include_blank = not (self.has_default() or "initial" in kwargs)
            # defaults = {"choices": self.get_choices(include_blank=include_blank)}

            # Many of the subclass-specific formfield arguments (min_value,
            # max_value) don't apply for choice fields, so be sure to only pass
            # the values that TypedChoiceField will understand.

            for k in list(kwargs):
                if k not in (
                        "coerce",
                        "empty_value",
                        "choices",
                        "required",
                        "widget",
                        "label",
                        "initial",
                        "help_text",
                        "error_messages",
                        "show_hidden_initial",
                        "disabled",
                        "max_length"
                ):
                    del kwargs[k]

            kwargs.update({
                'form_class': self.form_class,
                'choices': choices,
                'coerce': self.to_python
            })

        return super(JSONField, self).formfield(**kwargs) # noqa

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()

        kwargs['choices_function_name'] = self.choices_function.function_path

        return name, path, args, kwargs
