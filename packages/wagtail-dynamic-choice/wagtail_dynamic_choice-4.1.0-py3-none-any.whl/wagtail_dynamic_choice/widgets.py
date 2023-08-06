
from django import forms
from wagtail.telepath import register
from wagtail.widget_adapters import WidgetAdapter

from .function_specifier import FunctionSpecifier

from .apps import get_app_label

__all__ = ['DynamicChoiceWidget']

APP_LABEL = get_app_label()


class DynamicChoiceWidget(forms.widgets.Widget):
    template_name = APP_LABEL + "/widgets/dynamic_choice_widget.html"

    def __init__(self, choices_function_name, attrs=None):
        super().__init__(attrs)
        self.choices_function = FunctionSpecifier(function_path=choices_function_name)


class DynamicChoiceWidgetAdapter(WidgetAdapter):
    js_constructor = APP_LABEL + ".widgets.DynamicChoiceWidget"


register(DynamicChoiceWidgetAdapter(), DynamicChoiceWidget)