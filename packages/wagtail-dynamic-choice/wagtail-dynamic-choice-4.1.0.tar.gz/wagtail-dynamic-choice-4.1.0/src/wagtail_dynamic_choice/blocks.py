
from django import forms
from django.utils.functional import cached_property

from wagtail.blocks import FieldBlock
from wagtail.snippets.blocks import SnippetChooserBlock


from .form_fields import DynamicChoiceField
from .function_specifier import FunctionSpecifier

__all__ = ['AlternateSnippetChooserBlock', 'DynamicMultipleChoiceBlock']


class AlternateSnippetChooserBlock(SnippetChooserBlock):

    class Meta:
        identifier_field_name = 'identifier'
        use_identifier_as_value = False

    def _load_instance(self, value):

        try:
            kwargs = {self.meta.identifier_field_name: value}
            return self.model_class.objects.get(**kwargs)
        except self.model_class.DoesNotExist:
            return None

    def to_python(self, value):
        # the incoming serialised value should be None or an ID
        if value is None:
            return value
        elif not self.meta.use_identifier_as_value:
            return self._load_instance(value)

        return value

    def bulk_to_python(self, values):
        """Return the model instances for the given list of primary keys.

        The instances must be returned in the same order as the values and keep None values.
        """

        if self.meta.use_identifier_as_value:
            return list(values)

        objects = self.model_class.objects.in_bulk(values, field_name=self.meta.identifier_field_name)
        return [
            objects.get(name) for name in values
        ]  # Keeps the ordering the same as in values.

    def get_prep_value(self, value):
        # the native value (a model instance or None) should serialise to a PK or None
        if value is None:
            return None
        elif not self.meta.use_identifier_as_value:
            return getattr(value, self.meta.identifier_field_name)

        return value

    def value_from_form(self, value):

        value = super().value_from_form(value)

        if self.meta.use_identifier_as_value and value:
            value = getattr(value, self.meta.identifier_field_name)

        return value

    def get_form_state(self, value):

        if isinstance(value, str):
            kwargs = {self.meta.identifier_field_name: value}
            value = self.model_class.objects.get(**kwargs)

        return self.widget.get_value_data(value)

    def clean(self, value):

        if self.meta.use_identifier_as_value and value is not None and not isinstance(value, self.model_class):
            value = self._load_instance(value)

        value = super().clean(value)

        if self.meta.use_identifier_as_value and value is not None and isinstance(value, self.model_class):
            value = getattr(value, self.meta.identifier_field_name)

        return value

    def extract_references(self, value):

        if self.meta.use_identifier_as_value and value is not None and not isinstance(value, self.model_class):
            value = self._load_instance(value)

        return super().extract_references(value)

"""
DynamicChoiceBlockValue = str
forms.TypedMultipleChoiceField
class DynamicChoiceBlock(blocks.FieldBlock):

    def __init__(self, choices_function_name, **kwargs):
        self.field = DynamicChoiceField(choices_function_name=choices_function_name)
        super().__init__(**kwargs)
"""


class DynamicMultipleChoiceBlock(FieldBlock):

    class Meta:
        choices_function_name = None
        help_text = ""
        required = False

    @cached_property
    def choices_function(self):
        return FunctionSpecifier(function_path=self.meta.choices_function_name)

    def __init__(self, *, choices_function_name, **kwargs):
        super().__init__(choices_function_name=choices_function_name, **kwargs)

    @cached_property
    def field(self):
        return forms.TypedMultipleChoiceField(choices=self.choices_function,
                                              coerce=self.to_python,
                                              help_text=self.meta.help_text,
                                              required=self.meta.required)
