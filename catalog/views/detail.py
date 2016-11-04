from django.conf import settings
from django import forms
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django_mako_plus import view_function
from .. import dmp_render_to_string, dmp_render
from catalog import models as cmod
from . import initialize_template_vars

@view_function
def process_request(request):
    # Initialize Template vars
    template_vars = initialize_template_vars(request)

    try:
        p = cmod.Product.objects.get(id=request.urlparams[0])
    except cmod.Proudct.DoesNotExist:
        return HttpResponseRedirect('/catalog/index/')

    # Add to Last5 Viewed
    request.shopping_cart.item_viewed(p)

    template_vars['p'] = p
    return dmp_render(request, 'detail.html', template_vars)

### Carousel Method
@view_function
def carousel(request):
    # I'm sending p so I have access to the name for the modal title.
    p = cmod.Product.objects.get(id=request.urlparams[0])
    template_vars = {
        'p': p,
        'p_images': cmod.ProductImage.objects.all().filter(product=p),
    }
    return dmp_render(request, 'detail.carousel.html', template_vars)
