from django.http import JsonResponse
from django.conf import settings
from catalog import models as cmod

def process_request(request):

    # Get variables off of request
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

    resultslist = []

    for p in products:
        prod_info = {}
        prod_info['name'] = p.name
        prod_info['type'] = p.__class__.ClassName
        prod_info['description'] = p.description
        prod_info['price'] = p.price
        prod_info['add_date'] = p.add_date
        prod_info['category'] = p.category
        resultslist.append(prod_info)

    return JsonResponse(resultslist)

# class APIForm(forms.Form):
#     name = forms.CharField(required=False)
#     minprice = forms.DecimalField(required=False)
#     maxprice = forms.DecimalField(required=False)
#     category = forms.CharField(required=False)
