from django import template
register = template.Library()


@register.simple_tag
def setvar(value=None):
    """Assignment to a variable"""
    return value
