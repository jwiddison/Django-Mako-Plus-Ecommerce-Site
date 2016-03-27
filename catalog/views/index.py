from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response
from catalog import models as cmod
from catalog.views import translate_product


@view_function
def process_request(request):

    # Get list of products
    products = cmod.Product.objects.all().not_instance_of(cmod.RentalProduct).order_by('name')

    # filter to current category, if there is one
    if request.urlparams[0]:
        products = products.filter(category=request.urlparams[0])


    # Translate p.id list into list of objects
    recent_products_list = translate_product(request)

    template_vars = {
      'products': products,
      'categories': cmod.Category.objects.all().order_by('name'),
      'recent_products_list': recent_products_list,
    }
    return dmp_render_to_response(request, 'index.html', template_vars)
