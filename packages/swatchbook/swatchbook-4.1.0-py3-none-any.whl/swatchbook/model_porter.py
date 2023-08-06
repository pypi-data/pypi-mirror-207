import os
import re

from model_porter.config import ModelPorterConfig
from model_porter.repository import file_reader_from_path, UndefinedReference

from wagtail_attachments.models.attachment_roles import AttachmentRole
from wagtail_attachments.models.attachment_fields import ContentAttachmentFile

from .blocks import ConditionalColourBlock, ColourBlock, ConditionalVariableBlock
from .models import FontFace, FontFaceAttachment, FontFamily

from .utilities import parse_colour_block_value as parse_colour_block_value_impl


def load_font_family(*, name):
    result = FontFamily.objects.get(name=name)
    return result


def build_font_face_attachment(*, specifier, context, role_identifier):

    role = AttachmentRole.objects.get(identifier=role_identifier)
    font_face = context.get_variable(context.INSTANCE_VARIABLE)

    reader = file_reader_from_path(specifier, context)
    data = reader.read()
    file = ContentAttachmentFile(data, name=os.path.basename(specifier))

    attachment = FontFaceAttachment()
    attachment.model = font_face
    attachment.role_id = role.id
    attachment.file = file

    return [attachment]


def build_font_face_attachments(*, specifiers, context, role_identifier):

    result = []

    for specifier in specifiers:
        result.extend(build_font_face_attachment(specifier=specifier, context=context, role_identifier=role_identifier))

    return result


def build_font_faces(*, specifiers, context):

    family = context.get_variable(context.INSTANCE_VARIABLE)
    font_faces = []

    for specifier in specifiers:
        font_style, font_weight, font_formats = specifier

        font_face = FontFace()
        font_face.family = family
        font_face.style = font_style
        font_face.weight = font_weight

        context.push_variable(context.INSTANCE_VARIABLE, font_face)

        attachments = []

        for key, value in font_formats.items():
            attachments.extend(build_font_face_attachment(specifier=value, role_identifier=key, context=context))

        context.pop_variable(context.INSTANCE_VARIABLE)

        font_face.attachments = attachments
        font_faces.append(font_face)

    return font_faces


COLOUR_RE = re.compile(r'^(?P<type>(rgb|rgba|hsl|hsla))\((?P<values>[^)]*)\)$')
NUMERIC_RE = re.compile(r'^(?P<value>[0-9]+(.[0-9]+)?)(?P<unit>[^.0-9]*)$')

COLOUR_BLOCK = ColourBlock()


def parse_colour_block_value(*, specifier):

    result = parse_colour_block_value_impl(specifier=specifier)

    result = COLOUR_BLOCK.to_python(result)

    return result


def parse_colour_definition_value(*, specifier):
    pass


CONDITIONAL_COLOUR_BLOCK = ConditionalColourBlock()


def build_conditional_colours(*, specifiers, context):
    colours = []

    for specifier in specifiers:
        media_query, colour_value = specifier

        instance = context.get_instance(media_query, None)

        if instance is None:
            raise UndefinedReference(media_query)

        colour_value = parse_colour_block_value(specifier=colour_value)
        colour = CONDITIONAL_COLOUR_BLOCK.to_python({'query': instance.id, 'colour': colour_value})
        colours.append(('conditional_definition', colour))

    return colours


CONDITIONAL_VARIABLE_BLOCK = ConditionalVariableBlock()


def build_conditional_variables(*, specifiers, context):
    variables = []

    for specifier in specifiers:
        media_query, definition = specifier

        instance = context.get_instance(media_query, None)

        if instance is None:
            raise UndefinedReference(media_query)

        variable = CONDITIONAL_VARIABLE_BLOCK.to_python({'query': instance.id, 'definition': definition})
        variables.append(('conditional_definition', variable))

    return variables


class SwatchbookConfig(ModelPorterConfig):

    def __init__(self, app_label, module):
        super(SwatchbookConfig, self).__init__(app_label, module)
        self.register_function_action(build_font_faces, context_argument='context')
        self.register_function_action(build_font_face_attachment, context_argument='context')
        self.register_function_action(build_font_face_attachments, context_argument='context')
        self.register_function_action(load_font_family)
        self.register_function_action(parse_colour_block_value)
        self.register_function_action(build_conditional_colours, context_argument='context')
        self.register_function_action(build_conditional_variables, context_argument='context')
