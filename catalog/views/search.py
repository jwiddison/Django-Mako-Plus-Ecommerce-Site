from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django_mako_plus import view_function
from .. import dmp_render_to_string, dmp_render
from catalog import models as cmod
from . import initialize_template_vars


@view_function
def process_request(request):
    # Initialize template vars.  (Includes category)
    template_vars = initialize_template_vars(request)

    # Get query string off of URL
    q = request.GET.get('q','')

    # Get list of products that match the query
    products = cmod.Product.objects.all().not_instance_of(cmod.RentalProduct).order_by('name').filter(name__icontains = q)

    template_vars['products'] = products
    return dmp_render(request, 'search.html', template_vars)
