from django import template
from django.urls import reverse
register = template.Library()


@register.simple_tag
def abs_url(value, request, **kwargs):
    return reverse(value, kwargs=kwargs)
