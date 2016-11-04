from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django_mako_plus import view_function
from .. import dmp_render_to_string, dmp_render
from catalog import models as cmod


@view_function
def process_request(request):

    events = cmod.Event.objects.all().order_by('start_date')

    # Send Sale to the template
    template_vars = {
        'events': events,
    }
    return dmp_render(request, 'upcomingevents.html', template_vars)
