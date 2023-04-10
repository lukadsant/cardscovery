import re
from django import template

register = template.Library()

@register.filter
def split(value, arg):
    return value.split(arg)

@register.filter
def re_sub(value, arg):
    return re.sub(r'\b__[^\s]+__\b', '', value)
