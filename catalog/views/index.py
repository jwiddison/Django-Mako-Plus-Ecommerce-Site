from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django_mako_plus import view_function
from .. import dmp_render_to_string, dmp_render
from catalog import models as cmod
from . import initialize_template_vars


@view_function
def process_request(request):
    # Initialize Template Vars
    template_vars = initialize_template_vars(request)

    # Get list of products
    products = cmod.Product.objects.all().not_instance_of(cmod.RentalProduct).order_by('name')

    # filter to current category, if there is one
    if request.urlparams[0]:
        products = products.filter(category=request.urlparams[0])

    template_vars['products'] = products
    return dmp_render(request, 'index.html', template_vars)
