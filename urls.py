#!/usr/bin/env python

from django.conf.urls.defaults import *
import views

urlpatterns = patterns('',
  url('^$', views.gallery_index),
)
