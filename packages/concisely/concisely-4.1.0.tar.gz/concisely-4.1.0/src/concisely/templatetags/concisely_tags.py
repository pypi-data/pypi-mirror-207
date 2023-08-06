
from django import template
from django.template.exceptions import TemplateSyntaxError

from django.utils.html import format_html
from django.templatetags.static import static

from django_auxiliaries.tags import register_simple_block_tag

from ..apps import get_app_label

APP_LABEL = get_app_label()

register = template.Library()


@register_simple_block_tag(register, name="heading", autoescape=False)
def heading_tag(context, nodelist, level, *, element_id=None, classname=None):
    try:
        level = int(level)
    except ValueError:
        level = 2

    if level < 1:
        level = 1
    elif level > 6:
        level = 6

    if element_id:
        element_id = f" id=\"{element_id}\""
    else:
        element_id = ''

    if classname:
        classname = f" class=\"{classname}\""
    else:
        classname = ''

    content = nodelist.render(context)
    result = f"<h{level:d}{element_id}{classname}>{content}</h{level:d}>"
    return result


@register.simple_tag(takes_context=False)
def concisely_support(*, container_element):

    if container_element == 'head':
        return format_html('<link rel="stylesheet" type="text/css" href="{}">',
                           static(APP_LABEL + '/css/concisely.css'))

    return ''

