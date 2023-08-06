import json

from django import forms
from django.utils.functional import cached_property


from wagtail import blocks

from wagtail.admin.staticfiles import versioned_static
from wagtail.telepath import register

from wagtail.snippets.blocks import SnippetChooserBlock

from wagtail_switch_block.blocks import SwitchBlock, SwitchValue, TYPE_FIELD_NAME
from wagtail_dynamic_choice.blocks import AlternateSnippetChooserBlock

from model_porter.support_mixin import ModelPorterSupportMixin

from django_auxiliaries.templatetags.django_auxiliaries_tags import tagged_static

from .utilities import parse_colour_block_value
from .widgets import ColourInput

from .apps import get_app_label

__all__ = ['ColourSchemeChoiceBlock', 'MediaCondition', 'RGBBlock', 'RGBABlock', 'HSLBlock', 'HSLABlock',
           'ColourBlock', 'ColourBlockValue', 'ColourDefinitionBlock',
           'ConditionalColourBlock',
           'ResponsiveColourBlock', 'ResponsiveColourValue',
           'ConditionalVariableBlock',
           'define_css_color']

APP_LABEL = get_app_label()


class ColourSchemeChoiceBlock(blocks.ChoiceBlock):

    choices = [
        ('light', 'Light'),
        ('dark', 'Dark'),
    ]


class MediaCondition(blocks.StructBlock):

    class Meta:
        verbose_name = 'Media Condition'
        verbose_name_plural = 'Media Conditions'

    colour_scheme = ColourSchemeChoiceBlock(label="Colour Scheme", required=False)

    def deconstruct(self):
        path, args, kwargs = blocks.Block.deconstruct(self)
        return path, args, kwargs


class RGBBlock(blocks.StructBlock):

    class Meta:
        verbose_name = 'RGB colour'
        verbose_name_plural = 'RGB colours'

    red = blocks.DecimalBlock(label='Red', required=True, default=255, min_value=0, max_value=255)
    green = blocks.DecimalBlock(label='Green', required=True, default=255, min_value=0, max_value=255)
    blue = blocks.DecimalBlock(label='Blue', required=True, default=255, min_value=0, max_value=255)

    def deconstruct(self):
        path, args, kwargs = blocks.Block.deconstruct(self)
        return path, args, kwargs


class RGBABlock(blocks.StructBlock):

    class Meta:
        verbose_name = 'RGBA colour'
        verbose_name_plural = 'RGBA colours'

    red = blocks.DecimalBlock(label='Red', required=True, default=255, min_value=0, max_value=255)
    green = blocks.DecimalBlock(label='Green', required=True, default=255, min_value=0, max_value=255)
    blue = blocks.DecimalBlock(label='Blue', required=True, default=255, min_value=0, max_value=255)
    alpha = blocks.DecimalBlock(label='Alpha', required=True, default=1, min_value=0, max_value=1)

    def deconstruct(self):
        path, args, kwargs = blocks.Block.deconstruct(self)
        return path, args, kwargs


class HSLBlock(blocks.StructBlock):

    class Meta:
        verbose_name = 'HSL colour'
        verbose_name_plural = 'HSL colours'

    hue = blocks.DecimalBlock(label='Hue', required=True, default=0, min_value=0, max_value=360)
    saturation = blocks.DecimalBlock(label='Saturation', required=True, default=100, min_value=0, max_value=100)
    lightness = blocks.DecimalBlock(label='Lightness', required=True, default=50, min_value=0, max_value=100)

    def deconstruct(self):
        path, args, kwargs = blocks.Block.deconstruct(self)
        return path, args, kwargs


class HSLABlock(blocks.StructBlock):

    class Meta:
        verbose_name = 'HSLA colour'
        verbose_name_plural = 'HSLA colours'

    hue = blocks.DecimalBlock(label='Hue', required=True, default=0, min_value=0, max_value=360)
    saturation = blocks.DecimalBlock(label='Saturation', required=True, default=100, min_value=0, max_value=100)
    lightness = blocks.DecimalBlock(label='Lightness', required=True, default=50, min_value=0, max_value=100)
    alpha = blocks.DecimalBlock(label='Alpha', required=True, default=1, min_value=0, max_value=1)

    def deconstruct(self):
        path, args, kwargs = blocks.Block.deconstruct(self)
        return path, args, kwargs


class ColourBlockValue(SwitchValue):

    @property
    def as_css_string(self):
        return define_css_color(self)


class ColourBlock(SwitchBlock):

    class Meta:
        value_class = ColourBlockValue
        verbose_name = 'colour'
        verbose_name_plural = 'colours'

    rgb = RGBBlock(label="RGB")
    rgba = RGBABlock(label="RGBA")
    hsl = HSLBlock(label="HSL")
    hsla = HSLABlock(label="HSLA")

    def __init__(self, **kwargs):
        super(ColourBlock, self).__init__(**kwargs)
        self._colour_field = ColourFieldBlock(**kwargs)

    def deconstruct(self):
        path, args, kwargs = blocks.Block.deconstruct(self)
        return path, args, kwargs

    def set_name(self, name):
        super(ColourBlock, self).set_name(name)
        self._colour_field.set_name(name)

    def value_from_datadict(self, data, files, prefix):

        value = data.get(prefix, '{}')
        value = json.loads(value)
        result = self.to_python(value)
        return result

    def value_omitted_from_data(self, data, files, prefix):
        return prefix in data

    def get_form_state(self, value):
        state = super(ColourBlock, self).get_form_state(value)
        colour_type = state[TYPE_FIELD_NAME]

        if colour_type and not isinstance(colour_type, str):
            colour_type = colour_type[0]

        state[TYPE_FIELD_NAME] = colour_type

        return state

    # noinspection PyMethodMayBeStatic
    def from_repository(self, value, context):
        value = parse_colour_block_value(specifier=value)
        return value


class ColourFieldBlock(blocks.FieldBlock):

    class Meta:
        verbose_name = 'colour'
        verbose_name_plural = 'colours'

    def __init__(self, required=False, help_text=None, validators=(), **kwargs):

        self.field_options = {
            "required": required,
            "help_text": help_text,
            "validators": validators,
        }

        super(ColourFieldBlock, self).__init__(required=required, help_text=help_text, validators=validators, **kwargs)

    def deconstruct(self):
        path, args, kwargs = blocks.Block.deconstruct(self)
        return path, args, kwargs

    @cached_property
    def field(self):

        field_kwargs = {
            "widget": ColourInput(),
        }
        field_kwargs.update(self.field_options)
        return forms.CharField(**field_kwargs)


class ColourBlockAdapter(blocks.field_block.FieldBlockAdapter):
    js_constructor = APP_LABEL + '.blocks.ColourBlock'

    def js_args(self, block):
        result = super(ColourBlockAdapter, self).js_args(block._colour_field)
        return result

    @cached_property
    def media(self):
        return super().media + forms.Media(css={
            'all': [
                tagged_static(APP_LABEL + '/css/swatchbook.css'),
            ]
            },
            js=[
            versioned_static('wagtailadmin/js/telepath/widgets.js'),
            tagged_static(APP_LABEL + '/js/swatchbook.js'),
        ])


register(ColourBlockAdapter(), ColourBlock)


class ColourDefinitionBlock(SwitchBlock):

    colour = ColourBlock(label="Colour", required=True)
    variable = AlternateSnippetChooserBlock(target_model=APP_LABEL + ".colour", use_identifier_as_value=True)

    # noinspection PyMethodMayBeStatic
    def define_css_expression(self, value, prefix=''):

        if prefix:
            prefix += '-'

        result = ''

        if value.type == 'colour':
            result = define_css_color(value.value)
        elif value.type == 'variable':
            result = "var(--{}{})".format(prefix, value.value)

        return result

    # noinspection PyMethodMayBeStatic
    def extract_css_variable(self, value, prefix=''):

        if prefix:
            prefix += '-'

        result = ''

        if value.type == 'variable':
            result = "--{}{}".format(prefix, value.value)

        return result


class ConditionalColourBlock(ModelPorterSupportMixin, blocks.StructBlock):

    query = SnippetChooserBlock(target_model=APP_LABEL + ".MediaQuery", label="Media Query", required=True)
    colour = ColourDefinitionBlock(label="Colour", required=True)

    def deconstruct(self):
        path, args, kwargs = blocks.Block.deconstruct(self)
        return path, args, kwargs

    def clean(self, value):
        value = super(ConditionalColourBlock, self).clean(value)
        return value

    # noinspection PyMethodMayBeStatic
    def from_repository(self, value, context):

        query = context.get_instance(value['query'])
        value['query'] = query.pk if query else None

        if isinstance(self.child_blocks['colour'], ModelPorterSupportMixin):
            value['colour'] = self.child_blocks['colour'].from_repository(value['colour'], context)

        return value


ResponsiveColourValue = blocks.StructValue


class ResponsiveColourBlock(ModelPorterSupportMixin, blocks.StructBlock):

    default = ColourDefinitionBlock(required=True)
    conditionals = blocks.StreamBlock([('conditional_colour', ConditionalColourBlock())],
                                      min_num=0, max_num=None, required=False)

    # noinspection PyMethodMayBeStatic
    def from_repository(self, value, context):

        if isinstance(self.child_blocks['default'], ModelPorterSupportMixin):
            value['default'] = self.child_blocks['default'].from_repository(value['default'], context)

        if isinstance(self.child_blocks['conditionals'], blocks.StreamBlock):

            conditionals = []

            for conditional in value['conditionals']:
                block = self.child_blocks['conditionals'].child_blocks[conditional['type']]
                block_value = conditional['value']

                if isinstance(block, ModelPorterSupportMixin):
                    block_value = block.from_repository(block_value, context)

                conditionals.append({'type': conditional['type'], 'value': block_value})

            value['conditionals'] = conditionals

        return value

    def deconstruct(self):
        path, args, kwargs = blocks.Block.deconstruct(self)
        return path, args, kwargs


HUE_FORMAT = [1, ""]
IDENTITY_FORMAT = [1, ""]
PERCENT_FORMAT = [1, "%"]

HUE = "hue"
SATURATION = "saturation"
VALUE = "value"
LIGHTNESS = "lightness"
ALPHA = "alpha"
RED = "red"
GREEN = "green"
BLUE = "blue"

CSS_FORMAT_MAP = {
    "hsv":  {HUE: HUE_FORMAT,      SATURATION: PERCENT_FORMAT,  VALUE: PERCENT_FORMAT},
    "hsl":  {HUE: HUE_FORMAT,      SATURATION: PERCENT_FORMAT,  LIGHTNESS: PERCENT_FORMAT},
    "rgb":  {RED: IDENTITY_FORMAT, GREEN: IDENTITY_FORMAT, BLUE: IDENTITY_FORMAT},
    "hsva": {HUE: HUE_FORMAT,      SATURATION: PERCENT_FORMAT,  VALUE: PERCENT_FORMAT,  ALPHA: IDENTITY_FORMAT},
    "hsla": {HUE: HUE_FORMAT,      SATURATION: PERCENT_FORMAT,  LIGHTNESS: PERCENT_FORMAT, ALPHA: IDENTITY_FORMAT},
    "rgba": {RED: IDENTITY_FORMAT, GREEN: IDENTITY_FORMAT, BLUE: IDENTITY_FORMAT, ALPHA: IDENTITY_FORMAT},
}

DEFAULT_COLOR_VALUES_MAP = {
    "hsv": {'hue': 0, 'saturation': 1, 'value': 1},
    "hsl": {'hue': 0, 'saturation': 1, 'lightness': 0.5},
    "rgb": {'red': 255, 'green': 255, 'blue': 255},
    "hsva": {'hue': 0, 'saturation': 1, 'value': 1, 'alpha': 1},
    "hsla": {'hue': 0, 'saturation': 1, 'lightness': 0.5, 'alpha': 1},
    "rgba": {'red': 255, 'green': 255, 'blue': 255, 'alpha': 1},
}


def define_css_color(block_value):

    color_model = block_value.get(TYPE_FIELD_NAME, None)
    color = block_value.get(color_model, None)

    if color_model is None or color is None:
        return None

    default_values = DEFAULT_COLOR_VALUES_MAP.get(color_model, None)
    css_format_map = CSS_FORMAT_MAP.get(color_model, None)

    if not default_values or not css_format_map:
        return None

    result = color_model + "("

    for key, default_value in default_values.items():
        value = color.get(key, None)

        if value is None:
            color[key] = default_value

        css_format = css_format_map[key]

        factor = css_format[0]
        units = css_format[1]

        if not result.endswith("("):
            result += ", "

        result += "{:f}".format(color[key] * factor) + units

    result += ")"
    return result


class ConditionalVariableBlock(blocks.StructBlock):

    query = SnippetChooserBlock(target_model=APP_LABEL + ".MediaQuery", label="Media Query", required=True)
    definition = blocks.TextBlock(required=True)

    def deconstruct(self):
        path, args, kwargs = blocks.Block.deconstruct(self)
        return path, args, kwargs

