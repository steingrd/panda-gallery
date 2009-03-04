
from django import template

register = template.Library()

@register.filter(name='as_flickr_link')
def as_flickr_link_filter(value):
    return "http://farm%(farm)s.static.flickr.com/%(server)s/%(id)s_%(secret)s_s.jpg" % value.attrib

@register.filter(name='as_flickr_user_link')
def as_flickr_user_link_filter(value):
    return "http://www.flickr.com/photos/%(owner)s/%(id)s" % value.attrib

@register.filter(name='as_title')
def as_title_filter(value):
    return value.attrib['ownername'] + ' - ' + value.attrib['title']
