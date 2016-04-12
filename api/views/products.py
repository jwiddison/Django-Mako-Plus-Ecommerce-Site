from django.conf import settings
from django.http import JsonResponse
from django.core import serializers
from django_mako_plus.controller import view_function
from django.http import HttpResponse
from catalog import models as cmod
import json


@view_function
def process_request(request):

    # Get all the products
    products = cmod.Product.objects.all()

    # Product Name (partial, case-insensitve)
    if request.GET.get('name'):
        name = request.GET.get('name', '')
        products = products.filter(name__icontains = name)

    # Min Price
    if request.GET.get('minprice'):
        minprice = request.GET.get('minprice', '')
        products = products.filter(price__gte = minprice)

    # Max Price
    if request.GET.get('maxprice'):
        maxprice = request.GET.get('maxprice', '')
        products = products.filter(price__lte = maxprice)

    # Category Name (partial, case-insensitve)
    if request.GET.get('category'):
        category = request.GET.get('category', '')
        products = products.filter(category__name__icontains = category)

    resultslist = []

    for p in products:
        prod_info = {}
        prod_info['name'] = p.name
        prod_info['type'] = p.__class__.className
        prod_info['description'] = p.description
        prod_info['price'] = '$' + str(p.price)
        prod_info['add_date'] = str(p.add_date)
        prod_info['category'] = p.category.name
        resultslist.append(prod_info)

    # print(resultslist)

    data = json.dumps(resultslist)

    return HttpResponse(data, content_type='application/json')
