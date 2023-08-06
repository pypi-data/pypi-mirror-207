from django import template

from ..apps import get_app_label

__all__ = ['draftail_maths_support_tag']

APP_LABEL = get_app_label()

register = template.Library()

SUPPORT_TEMPLATE_SETTING = APP_LABEL + '/tags/support.html'
MATHJAX_VERSION_SETTING = '3.2.1'


@register.inclusion_tag(SUPPORT_TEMPLATE_SETTING, name="draftail_maths_support")
def draftail_maths_support_tag(*, container_element, is_admin_page=False, mathjax_version=MATHJAX_VERSION_SETTING):

    result = {
        'container_element': container_element,
        'is_admin_page': is_admin_page,
        'mathjax_version': mathjax_version,
        'is_mathjax_version_2': mathjax_version.startswith('2.'),
        'is_mathjax_version_3': mathjax_version.startswith('3.')
    }

    return result
