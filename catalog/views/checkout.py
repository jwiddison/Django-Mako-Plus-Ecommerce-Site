from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response
from catalog import models as cmod
from catalog.views import translate_product
from django import forms


@view_function
def process_request(request):

    # Get lists to send to template

    products = cmod.Product.objects.all().not_instance_of(cmod.RentalProduct).order_by('name')
    categories = cmod.Category.objects.all().order_by('name')
    images = cmod.ProductImage.objects.all()
    form = CheckoutForm()


    # Translate p.id list into list of objects (for last 5)
    recent_products_list = translate_product(request)

    template_vars = {
      'products': products,
      'categories': categories,
      'images': images,
      'recent_products_list': recent_products_list,
      'form': form,

    }
    return dmp_render_to_response(request, 'checkout.html', template_vars)


class CheckoutForm(forms.Form):
    shipping_name = forms.CharField(label='Shipping Name', max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Shipping Name', 'class': 'form-control'}))
    shipping_address = forms.CharField(label='Shipping Address', required=True, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Shipping Address', 'class': 'form-control'}))
    shipping_city = forms.CharField(label='Shipping City', required=True, widget=forms.TextInput(attrs={'placeholder': 'Shipping City', 'class': 'form-control'}))
    shipping_state = forms.CharField(label='Shipping State', required=True, widget=forms.TextInput(attrs={'placeholder': 'Shipping State', 'class': 'form-control'}))
    shipping_zip_code = forms.CharField(label='Shipping Zip Code', required=True, widget=forms.TextInput(attrs={'placeholder': 'Shippping Zip Code', 'class': 'form-control'}))
