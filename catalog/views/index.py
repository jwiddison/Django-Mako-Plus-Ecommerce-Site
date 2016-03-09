from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django_mako_plus.controller import view_function
from django.contrib.auth.decorators import permission_required
from .. import dmp_render, dmp_render_to_response
from catalog import models as cmod


@view_function
@permission_required('catalog.change_product', login_url='/homepage/index/')
def process_request(request):
    category_id = request.urlparams[0]
    if str(category_id) == '':
        pass
    else:
        try:
            category = cmod.Category.objects.get(id=request.urlparams[0])
        except cmod.Category.DoesNotExist:
            return HttpResponseRedirect('/catalog/index/')

    products = cmod.Product.objects.all().order_by('name')

    # Filter out rental products
    # for p in products:
    #     if p.__class__.className == 'Rental Product':
    #         products.remove(p)

    # Filter for the id number of the category in the URL if someone has selected one.
    print(category_id)
    if str(category_id) == '':
        pass
    else:
        products = products.filter(category = category_id)

    # Get other lists to send to template
    categories = cmod.Category.objects.all().order_by('name')
    images = cmod.ProductImage.objects.all()


    template_vars = {
      'products': products,
      'categories': categories,
      'images': images,
    }
    return dmp_render_to_response(request, 'index.html', template_vars)
