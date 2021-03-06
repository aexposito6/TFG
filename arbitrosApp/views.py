# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.files import File
from django.shortcuts import render

import json
import string
import urllib2


from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

from forms import UserForm
import models
import os


@csrf_exempt
def register(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()

    # Render the template depending on the context.
    return render_to_response(
        'registration/register.html',
        {'user_form': user_form, 'registered': registered},
        context)



def homepage(request):
    context = RequestContext(request)
    return render_to_response("homepage.html",{}, context)

def save_videos():
    models.Videos.objects.all().delete()
    path = "/home/antonio/PycharmProjects/TFG/arbitrosApp/static"
    arr = os.listdir(path)
    for i in arr:
        file_to_save = open(os.path.join(path, i),'rb').read()
        video = models.Videos(path="..static"+ "/"+ i ,video=File(file_to_save), name=i)
        video.save()


def list_videos(request):
    l=[]
    save_videos()
    for i in models.Videos.objects.all():
        l.append(i)

    return render(request, "list_videos.html", {'video': l})
