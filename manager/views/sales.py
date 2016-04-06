from django.conf import settings
from django import forms
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django_mako_plus.controller import view_function
from django.contrib.auth.decorators import permission_required
from .. import dmp_render, dmp_render_to_response
from catalog import models as cmod
from account import models as amod
import datetime

################################################################################################
############### Products Homepage ##############################################################
################################################################################################
@view_function
@permission_required('catalog.change_sale', login_url='/homepage/index/')
def process_request(request):
    '''List the users in a table on the screen '''
    products = cmod.Product.objects.all().order_by('name')
    images = cmod.ProductImage.objects.all()

    template_vars = {
      'products': products,
      'images': images,
    }
    return dmp_render_to_response(request, 'products.html', template_vars)
