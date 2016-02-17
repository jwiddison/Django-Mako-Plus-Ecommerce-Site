from django.conf import settings
from django import forms
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response
from catalog import models as cmod
import datetime

#
# events Home Page
#

@view_function
def process_request(request):
    '''List the users in a table on the screen '''
    events = cmod.Event.objects.all().order_by('name')


    template_vars = {
      'events': events,
    }
    return dmp_render_to_response(request, 'events.html', template_vars)