from django.conf import settings
from django import forms
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response
from catalog import models as cmod
from catalog.views import translate_product



@view_function
def process_request(request):
    # Get lists to return to the template_vars
    categories = cmod.Category.objects.all().order_by('name')
    images = cmod.ProductImage.objects.all()



    # Get the product that we're working with and send it to template
    p = cmod.Product.objects.get(id=request.urlparams[0])

    # Create a list in the session dictionary.  Get's the list if its already there, or an empty list if there isn't one yet.
    rv = request.session.get('recently_viewed', [])
    # If the id of our product is already in the recently_viewed list, remove it
    if p.id in rv:
        rv.remove(p.id)
    # else:
    # if the list is more than five long, remove the oldest one.
    if rv.__len__() >= 5:
        rv.pop(0)

    #Add our product to the list.
    rv.append(p.id)

    # Save our list into the session dictionary with the key "recently_viewed"
    request.session['recently_viewed'] = rv


    # Translate p.id list into list of objects (calling function written in __init__.py)
    recent_products_list = translate_product(request)

    template_vars = {
    #   'products': products,
      'categories': categories,
      'images': images,
      'p_images': cmod.ProductImage.objects.all().filter(product=p),
      'p': p,
      'recent_products_list': recent_products_list,
    }
    return dmp_render_to_response(request, 'detail.html', template_vars)


@view_function
def carousel(request):

    p = cmod.Product.objects.get(id=request.urlparams[0])

    template_vars = {
        'p': p,
        'p_images': cmod.ProductImage.objects.all().filter(product=p),
    }
    return dmp_render_to_response(request, 'detail.carousel.html', template_vars)
