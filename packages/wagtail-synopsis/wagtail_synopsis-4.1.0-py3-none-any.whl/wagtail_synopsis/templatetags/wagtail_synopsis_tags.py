from django import template
from django.templatetags.static import static

from ..apps import get_app_label

APP_LABEL = get_app_label()

register = template.Library()


@register.simple_tag(takes_context=False, name="synopsis_destination_url")
def synopsis_destination_url_tag(synopsis, request=None, site=None):
    return synopsis.determine_destination_url(request, site)


def gather_style_sheets():

    urls = [
            # static(APP_LABEL + '/css/synopsis_list.css')
    ]

    return urls


def gather_scripts():

    urls = []

    return urls


SUPPORT_TEMPLATE_SETTING = APP_LABEL + '/tags/support.html'


@register.inclusion_tag(SUPPORT_TEMPLATE_SETTING, name="wagtail_synopsis_support")
def wagtail_synopsis_support_tag(*, container_element, is_admin_page=False):

    result = {
        'container_element': container_element,
        'is_admin_page': is_admin_page,
        'stylesheets': gather_style_sheets(),
        'scripts': gather_scripts()
    }

    return result