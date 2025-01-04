from django import template

register = template.Library()

@register.filter
def to_hours(duration):
    return duration / 60
