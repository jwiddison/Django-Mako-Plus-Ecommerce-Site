from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django_mako_plus import view_function
from .. import dmp_render_to_string, dmp_render
from catalog import models as cmod
from . import initialize_template_vars

@view_function
def process_request(request):
    template_vars = initialize_template_vars(request)
    return dmp_render(request, 'empty_cart.html', template_vars)
