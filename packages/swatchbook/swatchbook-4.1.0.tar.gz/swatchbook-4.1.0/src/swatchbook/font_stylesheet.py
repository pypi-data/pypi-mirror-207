import os

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from django.http import Http404


def update_font_stylesheet_file():

    text = build_stylesheet_definitions()
    file = ContentFile(text)
    save_file("swatchbook/fonts.css", file)


def format_css_font_source(url, font_format):

    return 'url("{}") format("{}")'.format(url, font_format)


def format_css_font_face(font_family, font_style, font_weight, sources):

    return ('@font-face {{ \n' +
            '   font-family: "{font_family}";\n' +
            '   font-style:  {font_style};\n' +
            '   font-weight:  {font_weight};\n' +
            '   src: {sources};\n' +
            '}}\n'
            ).format(font_family=font_family,
                     font_style=str(font_style),
                     font_weight=str(font_weight),
                     sources=sources)


def build_stylesheet_definitions(families=None):

    from .models import FontFamily

    if families is None:
        families = FontFamily.objects.all()

    families = families.order_by('name')

    css_declarations_per_family = {}

    css_declarations = []

    for family in families:

        family_decls = css_declarations_per_family.setdefault(family.name, [])

        for face in family.faces.all():

            sources = []

            for attachment in face.attachments.all():
                role = attachment.role.identifier
                font_path = "/media/" + attachment.file.name
                source = format_css_font_source(font_path, role)
                sources.append(source)

            css_font_face = format_css_font_face(
                font_family="__FAMILY__",
                font_style=face.style,
                font_weight=face.weight,
                sources=",\n".join(sources)
            )

            family_decls.append(css_font_face)

            css_font_face = css_font_face.replace("__FAMILY__", family.name)
            css_declarations.append(css_font_face)

    from .models import FontAlias

    aliases = FontAlias.objects.all()

    for alias in aliases:
        target = alias.family

        if target is None:
            continue

        family_decls = css_declarations_per_family.setdefault(target.name, [])

        for css_font_face in family_decls:
            css_font_face = css_font_face.replace("__FAMILY__", alias.alias)
            css_declarations.append(css_font_face)

    css_declarations = "\n".join(css_declarations)
    result = '@charset "UTF-8";\n\n{}\n'.format(css_declarations)
    return result


def save_file(local_path, content):

    available_path = default_storage.get_available_name(local_path)

    if local_path != available_path:
        default_storage.delete(local_path)

    try:
        local_path = default_storage.path(local_path)
    except NotImplementedError:
        local_path = None

    if local_path is None:
        raise Http404

    file = default_storage.save(local_path, content)
    return file
