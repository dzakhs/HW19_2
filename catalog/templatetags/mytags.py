
from django import template


register = template.Library()

@register.simple_tag(name='media_path')
def mediapath(image_path):
    return f"/media/{image_path}"


#@register.filter(name='media_path')
#def mediapath(image_path):
#    return f"/media/{image_path}"
