from django.conf import settings
from django import forms
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django_mako_plus.controller import view_function
from django.contrib.auth.decorators import permission_required
from .. import dmp_render, dmp_render_to_response
from catalog import models as cmod
from catalog.views import translate_product



@view_function
@permission_required('catalog.change_product', login_url='/homepage/index/')
def process_request(request):
    # Get lists to return to the template_vars
    products = cmod.Product.objects.all().order_by('name')
    categories = cmod.Category.objects.all().order_by('name')
    images = cmod.ProductImage.objects.all()

    # Get the product that we're working with and send it to template
    p = cmod.Product.objects.get(id=request.urlparams[0])


    rv = request.session.get('recently_viewed', [])
    if p.id in rv:
        rv.remove(p.id)
    # else:
    if rv.__len__() >= 5:
        rv.pop(0)

    rv.append(p.id)

    request.session['recently_viewed'] = rv

    # Translate p.id list into list of objects
    recent_products_list = translate_product(request)

    template_vars = {
      'products': products,
      'categories': categories,
      'images': images,
      'p': p,
      'recent_products_list': recent_products_list,
    }
    return dmp_render_to_response(request, 'detail.html', template_vars)
