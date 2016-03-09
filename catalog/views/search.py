from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django_mako_plus.controller import view_function
from django.contrib.auth.decorators import permission_required
from .. import dmp_render, dmp_render_to_response
from catalog import models as cmod


@view_function
@permission_required('catalog.change_product', login_url='/homepage/index/')
def process_request(request):

    # Get lists to send over
    products = cmod.Product.objects.all().order_by('name')
    categories = cmod.Category.objects.all().order_by('name')
    images = cmod.ProductImage.objects.all().order_by('name')

    # Get query off of URL
    q = request.GET.get('q','')

    count = products.count()

    template_vars = {
      'products': products,
      'categories': categories,
      'images': images,
      'q': q,
      'count': count,
    }
    return dmp_render_to_response(request, 'search.html', template_vars)



# ONLY Search by product name
