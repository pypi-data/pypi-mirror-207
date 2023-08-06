
from django import template

from django.utils.html import format_html
from django.templatetags.static import static

from ..apps import get_app_label


APP_LABEL = get_app_label()

register = template.Library()


@register.simple_tag(takes_context=False, name="adede_support")
def adede_support_tag(*, container_element):

    if container_element == 'head':
        return format_html('<link rel="stylesheet" type="text/css" href="{}">',
                           static(APP_LABEL + '/css/adede.css'))

    if container_element == 'body':
        return format_html('<script type="text/javascript" src="{}"></script>',
                           static(APP_LABEL + '/js/adede.js'))

    return ''

