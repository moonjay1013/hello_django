from django import template
from django.utils.safestring import mark_safe

register = template.Library()  # register的名字是固定的,不可改变


@register.filter
def my_filter(v1, v2):
    return v1 + v2


@register.simple_tag
def my_simple_tag(v1, v2, v3):
    return v1 + v2 + v3


@register.simple_tag
def my_html(v1, v2):
    temp_html = "<input type='text' id='%s' class='%s' />" % (v1, v2)
    return mark_safe(temp_html)
