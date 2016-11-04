from django.conf import settings
from django_mako_plus import view_function
from django import forms
from django.http import HttpResponseRedirect
from .. import dmp_render_to_string, dmp_render
from account.models import User


@view_function
def process_request(request):
    # Make sure user is logged in
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/account/login/')


    template_vars = {

    }
    return dmp_render(request, 'index.html', template_vars)
