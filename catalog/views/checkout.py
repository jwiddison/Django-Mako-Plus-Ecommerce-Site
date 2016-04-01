from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response
from catalog import models as cmod
from . import initialize_template_vars
from django.contrib.auth.decorators import login_required
from django import forms
import googlemaps
import requests


@view_function
def process_request(request):
    # Make sure user is logged in
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/catalog/login')

    # Make sure cart isn't empty
    if request.shopping_cart.cart == []:
        return HttpResponseRedirect('/catalog/empty_cart')

    # Initialize Template Vars
    template_vars = initialize_template_vars(request)

    form = ShippingForm()
    if request.method == 'POST':
        form = ShippingForm(request.POST)
        if form.is_valid():
            # Create an instance of google maps
            gmaps = googlemaps.Client(key=settings.GOOGLE_SERVER_KEY)

            # Get full, concatenated Address
            full_address = form.cleaned_data.get('shipping_address') + ', ' + form.cleaned_data.get('shipping_city') + ', ' + form.cleaned_data.get('shipping_state')
            geocode_result = gmaps.geocode(full_address)
            data = geocode_result.json()

            print(data)

            return HttpResponseRedirect('/catalog/checkout.payment')

    template_vars['form'] = form
    return dmp_render_to_response(request, 'checkout.html', template_vars)


class ShippingForm(forms.Form):
    shipping_name = forms.CharField(label='Shipping Name', max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Shipping Name', 'class': 'form-control'}))
    shipping_address = forms.CharField(label='Shipping Address', required=True, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Shipping Address', 'class': 'form-control'}))
    shipping_city = forms.CharField(label='Shipping City', required=True, widget=forms.TextInput(attrs={'placeholder': 'Shipping City', 'class': 'form-control'}))
    shipping_state = forms.CharField(label='Shipping State', required=True, widget=forms.TextInput(attrs={'placeholder': 'Shipping State', 'class': 'form-control'}))
    shipping_zip_code = forms.CharField(label='Shipping Zip Code', required=True, widget=forms.TextInput(attrs={'placeholder': 'Shipping Zip Code', 'class': 'form-control'}))

    # need to add clean methods to make sure the quantity is available.

@view_function
@login_required(login_url='/catalog/login/')
def payment(request):
    template_vars = initialize_template_vars(request)
    return dmp_render_to_response(request, 'checkout.payment.html', template_vars)
