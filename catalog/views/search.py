from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response
from catalog import models as cmod
from catalog.views import translate_product


@view_function
def process_request(request):

    # Get other lists to send over
    categories = cmod.Category.objects.all().order_by('name')
    images = cmod.ProductImage.objects.all()

    # Get query string off of URL
    q = request.GET.get('q','')

    # Get list of products that match the query
    # products = cmod.Product.objects.all().order_by('name').filter(name__iexact = q) # Don't need this when using icontains
    products = cmod.Product.objects.all().not_instance_of(cmod.RentalProduct).order_by('name').filter(name__icontains = q)

    # Get count of products.
    count = products.count()

    # Translate p.id list into list of objects
    recent_products_list = translate_product(request)

    template_vars = {
      'products': products,
      'categories': categories,
      'images': images,
      'q': q,
      'count': count,
      'recent_products_list': recent_products_list,

    }
    return dmp_render_to_response(request, 'search.html', template_vars)



# ONLY Search by product name
