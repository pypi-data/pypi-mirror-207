
from django import template
from django.templatetags.static import static

from ..models import lookup_morsel


from ..apps import get_app_label


APP_LABEL = get_app_label()

register = template.Library()


@register.simple_tag(takes_context=True, name="morsel")
def parse_morsel_tag(context, *, morsel, request=None, page=None, **kwargs):

    morsel = lookup_morsel(morsel)

    if morsel is None:
        return ''

    if request is None:
        request = context.get('request', None)

    if page is None:
        page = context.get('page', None)

    return morsel.render(request, page, context=context.flatten(), **kwargs)


def gather_style_sheets():

    urls = []

    return urls


def gather_scripts():

    urls = []

    return urls


SUPPORT_TEMPLATE_SETTING = APP_LABEL + '/tags/support.html'

"""
@register.inclusion_tag(SUPPORT_TEMPLATE_SETTING, name="morsel_support")
def morsel_support_tag(*, container_element, is_admin_page=False):

    result = {
        'container_element': container_element,
        'is_admin_page': is_admin_page,
        'stylesheets': gather_style_sheets(),
        'scripts': gather_scripts()
    }

    return result
"""
