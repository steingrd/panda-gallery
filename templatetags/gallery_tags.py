
from django import template

register = template.Library()

@register.filter(name='as_flickr_link')
def as_flickr_link_filter(value):
    return "http://farm%(farm)s.static.flickr.com/%(server)s/%(id)s_%(secret)s_s.jpg" % value.attrib

    

