
from django import template

from ..apps import get_app_label

APP_LABEL = get_app_label()

register = template.Library()


def gather_style_sheets():

    urls = ["/media/swatchbook/variables.css",
            "/media/swatchbook/fonts.css",
            "/media/swatchbook/colours.css"]

    return urls


def gather_scripts():

    urls = []

    return urls


SUPPORT_TEMPLATE_SETTING = APP_LABEL + '/tags/support.html'


@register.inclusion_tag(SUPPORT_TEMPLATE_SETTING, name="swatchbook_support")
def swatchbook_support_tag(*, container_element, is_admin_page=False):

    result = {
        'container_element': container_element,
        'is_admin_page': is_admin_page,
        'stylesheets': gather_style_sheets(),
        'scripts': gather_scripts()
    }

    return result
