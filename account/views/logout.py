from django.conf import settings
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django import forms
from django_mako_plus import view_function
from .. import dmp_render_to_string, dmp_render
from account.models import User

@view_function
def process_request(request):
    # Logout the user
    logout(request)

    # Clear last 5 from session
    request.shopping_cart.last_5_ids = []

    # Redirect to the login page
    return HttpResponseRedirect('/homepage/index/')
