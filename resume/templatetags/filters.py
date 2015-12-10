from django import template

register = template.Library()

@register.filter(name="split")
def split(value):
    return value.split('\n')

@register.filter(name="is_positive")
def is_positive(value):
    return value > 0