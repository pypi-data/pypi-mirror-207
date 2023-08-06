
from django.utils.html import format_html

from wagtail import hooks

from django_auxiliaries.templatetags.django_auxiliaries_tags import tagged_static

from .apps import get_app_label

APP_LABEL = get_app_label()


@hooks.register("insert_editor_css")
def editor_css():
    return format_html(
        '<link rel="stylesheet" href="{}">',
        tagged_static(APP_LABEL + '/css/swatchbook.css')
    )


@hooks.register("insert_global_admin_css")
def admin_css():
    return format_html(
        '<link rel="stylesheet" href="{}">',
        '/media/' + APP_LABEL + '/admin_colours.css'
    )
