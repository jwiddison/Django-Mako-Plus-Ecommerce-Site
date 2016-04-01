from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response
from catalog import models as cmod
from . import initialize_template_vars


@view_function
def process_request(request):
    template_vars = initialize_template_vars(request)
    return dmp_render_to_response(request, 'receipt.html', template_vars)
