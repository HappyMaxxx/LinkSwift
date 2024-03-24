from django import template
from ..models import Link

register = template.Library()

@register.simple_tag
def top_links():
    links = Link.objects.order_by('-count')[:10]
    return links