from django import template
from django.templatetags.static import static

from django_auxiliaries.variable_scope import initialise_variable_scope

from ..apps import get_app_label

APP_LABEL = get_app_label()

register = template.Library()

SUPPORT_TEMPLATE_SETTING = APP_LABEL + '/tags/support.html'


@register.inclusion_tag(SUPPORT_TEMPLATE_SETTING, name="streetwise_support")
def streetwise_support_tag(*, container_element, is_admin_page=False):

    result = {
        'container_element': container_element,
        'is_admin_page': is_admin_page,
        'stylesheets': gather_style_sheets(),
        'scripts': gather_scripts()
    }

    if container_element == 'head':
        initialise_variable_scope(APP_LABEL, map_view_index=0)

    return result


def gather_style_sheets():

    urls = [static(APP_LABEL + "/css/streetwise.css")]

    """
from ..models.maps import MapViewer
    for layout in MapViewer.objects.all():
        attachments = layout.attachments_for_role_identifier('css')

        for stylesheet in attachments:
            urls.append(stylesheet.file.url)
    """

    return urls


def gather_scripts():

    urls = [static(APP_LABEL + "/js/streetwise.js")]

    """
from ..models.maps import MapViewer
    for layout in MapViewer.objects.all():
        attachments = layout.attachments_for_role_identifier('js')

        for script in attachments:
            urls.append(script.file.url)
    """

    return urls
