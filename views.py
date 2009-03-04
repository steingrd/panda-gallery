#!/usr/bin/env python

from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponse

from panda import get_panda_names, get_panda_photos

def gallery_index(request):
    available_pandas = get_panda_names()
    selected_panda = available_pandas[0]

    if 'panda' in request.GET:
        selected_panda = request.GET['panda']
 
    panda_photos = get_panda_photos(selected_panda)

    context = { 
        'selected_panda': selected_panda, 
        'available_pandas': available_pandas,
        'panda_photos': panda_photos
    }
    
    return render_to_response('panda_gallery/index.html', context)
