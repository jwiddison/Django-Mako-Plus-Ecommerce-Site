from django.conf import settings
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django import forms
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response
from account.models import User

@view_function
def process_request(request):
    # Logout the user
    logout(request)
    # Redirect to the login page
    return HttpResponseRedirect('/homepage/index/')
