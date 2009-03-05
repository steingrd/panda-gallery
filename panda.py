#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2009 by Steingrim Dovland <steingrd@ifi.uio.no>

import random

from django.conf import settings
from django.core.cache import cache

import flickrapi


def get_panda_names():
    flickr = flickrapi.FlickrAPI(settings.FLICKR_API_KEY)
    result = flickr.panda_getList()
    return [ elm.text for elm in result.getiterator('panda') ]


def get_panda_photos(panda_name):
    in_cache = cache.get(panda_name)
    if in_cache:
        return _get_panda_photos_from_xml(in_cache)

    flickr = flickrapi.FlickrAPI(settings.FLICKR_API_KEY)
    result = flickr.panda_getPhotos(panda_name=panda_name)
    photos = result.find('photos')

    timeout = int(photos.attrib['interval']) / 1000
    cache.set(panda_name, photos, timeout)

    return _get_panda_photos_from_xml(photos)


def _get_panda_photos_from_xml(photos):
    photo_list = photos.findall('photo')
    return photo_list[:settings.FLICKR_PANDA_PAGE]
