from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response
from catalog import models as cmod


@view_function
def process_request(request):

    events = cmod.Event.objects.all().order_by('start_date')

    # Send Sale to the template
    template_vars = {
        'events': events,
    }
    return dmp_render_to_response(request, 'upcomingevents.html', template_vars)
