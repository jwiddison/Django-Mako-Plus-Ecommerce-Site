from django.conf import settings
# from django_mako_plus.controller import view_function
# from django import forms
# from django.http import HttpResponseRedirect
# from .. import dmp_render, dmp_render_to_response
from catalog import models as cmod

def process_request(request):

    name = request.urlparams[0]
    minprice = request.urlparams[1]
    maxprice = request.urlparams[2]
    category = request.urlparams[3]

    # Product Name (partial, case-insensitve)
    if request.GET.get('name'):
        products = cmod.Product.objects.all().filter(name__icontains = name)

    # Min Price
    if request.GET.get('minprice'):
        products = cmod.Product.objects.all().filter(price >= minprice)

    # Max Price
    if request.GET.get('maxprice'):
        products = cmod.Product.objects.all().filter(price <= maxprice)

    # Category Name (partial, case-insensitve)
    if request.GET.get('category'):
        products = cmod.Product.objects.all().filter(category__icontains = category)

    return products
