from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response
from catalog import models as cmod
from catalog.views import translate_product


@view_function
def process_request(request):
    category_id = request.urlparams[0]
    if str(category_id) == '':
        pass
    else:
        try:
            category = cmod.Category.objects.get(id=request.urlparams[0])
        except cmod.Category.DoesNotExist:
            return HttpResponseRedirect('/catalog/index/')

    products = cmod.Product.objects.all().not_instance_of(cmod.RentalProduct).order_by('name')

    # Filter for the id number of the category in the URL if someone has selected one.
    print(category_id)
    if str(category_id) == '':
        pass
    else:
        products = products.filter(category = category_id)

    # Get other lists to send to template
    categories = cmod.Category.objects.all().order_by('name')
    images = cmod.ProductImage.objects.all()


    # Translate p.id list into list of objects
    recent_products_list = translate_product(request)

    template_vars = {
      'products': products,
      'categories': categories,
      'images': images,
      'recent_products_list': recent_products_list,

    }
    return dmp_render_to_response(request, 'index.html', template_vars)
