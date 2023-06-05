import os

from django import template

from HW19_2 import settings

register = template.Library()

@register.simple_tag(name='media_path')
def mediapath(image_path):
    media_url = settings.MEDIA_URL
    full_path = os.path.join(media_url, str(image_path))
    return full_path


#@register.filter(name='media_path')
#def mediapath(image_path):
#    return f"/media/{image_path}"
