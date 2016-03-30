from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response
from catalog import models as cmod
from . import initialize_template_vars

@view_function
def process_request(request):
    # Initialize Template Vars
    template_vars = initialize_template_vars(request)
    return dmp_render_to_response(request, 'cart.html', template_vars)

@view_function
def clear(request):
    request.shopping_cart.clear_items()
    return HttpResponseRedirect('/catalog/cart/')

@view_function
def remove(request):
    p = cmod.Product.objects.get(id=request.urlparams[0])
    request.shopping_cart.remove_item(p)
    return HttpResponseRedirect('/catalog/cart/')
