from django.conf import settings
# from django_mako_plus.controller import view_function
# from django import forms
# from django.http import HttpResponseRedirect
# from .. import dmp_render, dmp_render_to_response
from catalog import models as cmod

def process_request(request):

    # Not sure which of these I'm going to use, so I have both in here for now.
    name = request.urlparams[0]
    minprice = request.urlparams[1]
    maxprice = request.urlparams[2]
    category = request.urlparams[3]

    name = request.GET.get('name', '')
    minprice = request.GET.get('minprice', '')
    maxprice = request.GET.get('maxprice', '')
    category = request.GET.get('category', '')

    # Get all the products
    products = cmod.Product.objects.all()

    # Product Name (partial, case-insensitve)
    if request.GET.get('name'):
        products = products.filter(name__icontains = name)

    # Min Price
    if request.GET.get('minprice'):
        products = products.filter(price >= minprice)

    # Max Price
    if request.GET.get('maxprice'):
        products = products.filter(price <= maxprice)

    # Category Name (partial, case-insensitve)
    if request.GET.get('category'):
        products = products.filter(category__icontains = category)

    return products

class APIForm(forms.Form):
    name = forms.CharField(required=False)
    minprice = forms.DecimalField(required=False)
    maxprice = forms.DecimalField(required=False)
    category = forms.CharField(required=False)
