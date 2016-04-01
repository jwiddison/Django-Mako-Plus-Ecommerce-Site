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

            # Get info from form.
            name = form.cleaned_data.get('shipping_name')
            # Get address information from the form and clear out spaces
            address = form.cleaned_data.get('shipping_address')
            address.replace(" ", "+")
            city = form.cleaned_data.get('shipping_city')
            city.replace(" ", "+")
            state = form.cleaned_data.get('shipping_state')
            state.replace(" ", "+")
            zip_code = form.cleaned_data.get('shipping_zip_code')

            # Make full, concatenated Address
            full_address = address + ',+' + city + ',+' + state
            url="https://maps.googleapis.com/maps/api/geocode/json?address=%s" % full_address

            # Get results from google API and format them as JSON
            resp = requests.get(url)
            data = resp.json()

            ###################################################################
            #### Pull useable info out of the JSON response
            # House Number
            google_house_no = data['results'][0]['address_components'][0]['long_name']
            # Street
            google_street = data['results'][0]['address_components'][1]['short_name']
            # Combine two together for street address
            google_address = '%s %s' % (google_house_no, google_street)
            # City
            google_city = data['results'][0]['address_components'][2]['long_name']
            # State
            google_state = data['results'][0]['address_components'][4]['short_name']
            # Zip Code
            google_zip = data['results'][0]['address_components'][6]['long_name']

            # Get lists out of session
            google_response_list = request.session.get('google_address_response', [])
            user_address_list = request.session.get('user_input_address', [])

            # Override Lists from Session
            google_response_list = [name, google_address, google_city, google_state, google_zip]
            user_address_list = [name, address, city, state, zip_code]

            # Set Lists back into session.
            request.session['google_address_response'] = google_response_list
            request.session['user_input_address'] = user_address_list

            return HttpResponseRedirect('/catalog/checkout.shipping')

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
def shipping(request):
    template_vars = initialize_template_vars(request)
    return dmp_render_to_response(request, 'checkout.shipping.html', template_vars)


@view_function
@login_required(login_url='/catalog/login/')
def payment(request):
    template_vars = initialize_template_vars(request)

    if request.urlparams[0] == '1':
        useGoogle = True
    else:
        useGoogle = False

    template_vars['useGoogle'] = useGoogle
    return dmp_render_to_response(request, 'checkout.payment.html', template_vars)
