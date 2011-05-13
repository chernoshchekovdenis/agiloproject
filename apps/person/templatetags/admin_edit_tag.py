from django import template

register = template.Library()


@register.simple_tag
def edit_link(obj):
    url = '/admin/'
    url += str(obj._meta.app_label).lower()
    url += '/'
    url += str(obj._meta.object_name).lower()
    url += '/'
    url += str(obj.pk)
    return url
