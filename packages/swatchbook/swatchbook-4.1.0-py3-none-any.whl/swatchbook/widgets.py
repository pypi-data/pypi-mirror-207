from django.forms.widgets import HiddenInput, TextInput
from wagtail.telepath import register
from wagtail.widget_adapters import WidgetAdapter

__all__ = ['ColourInput', 'ColourInputAdapter']


class ColourInput(HiddenInput):

    def __init__(self):

        attrs = {
            "data-swatchbook-colour-input": True
        }

        super(ColourInput, self).__init__(attrs=attrs)


class ColourInputAdapter(WidgetAdapter):
    js_constructor = "swatchbook.widgets.ColourInput"

    def js_args(self, widget):
        result = super(ColourInputAdapter, self).js_args(widget)
        return result

register(ColourInputAdapter(), ColourInput)
