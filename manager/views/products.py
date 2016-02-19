from django.conf import settings
from django import forms
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response
from catalog import models as cmod
from account import models as amod
import datetime

#
# Products Home Page
#

@view_function
def process_request(request):
    '''List the users in a table on the screen '''
    products = cmod.Product.objects.all().order_by('name')


    template_vars = {
      'products': products,
    }
    return dmp_render_to_response(request, 'products.html', template_vars)


################################################
############### Create a Product ###############
################################################
@view_function
def create(request):
    '''Create a New Product'''
    # process the form
    form = CreateProductForm()
    if request.method == 'POST':   # if they've submitted the form
        form = CreateProductForm(request.POST) # Re-create the form with data in it
        if form.is_valid():  # Validate said form using validations specified in form object we created

            # create a temporary user object
            p = cmod.Product()

            # Fill user object with the data captured from the form
            p.name = form.cleaned_data.get('name')
            p.price = form.cleaned_data.get('price')
            p.description = form.cleaned_data.get('description')
            p.image = form.cleaned_data.get('image')

            # Update database with user object
            p.save()

            # Redirect to confirmation page (change once login above is working)
            return HttpResponseRedirect('/manager/products/')

    # parameters from the email back to the browser just in case we need them later.
    template_vars = {
      'form': form,
    }
    return dmp_render_to_response(request, 'products.create.html', template_vars)

class CreateProductForm(forms.Form):
    name = forms.CharField(label='Product Name', required=True, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Product Name'}))
    price = forms.CharField(label='Price', required=True, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Price'}))
    description = forms.CharField(label='Description', required=True, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Description'}))
    image = forms.CharField(label='Image', required=True, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Image'}))


################################################
################# Edit a Product ###############
################################################

@view_function
def edit(request):
    '''Edits a Product'''
    # Make sure that the ID number in the URL matches a user that actually exists
    try:
        product = cmod.Product.objects.get(id=request.urlparams[0])
    except cmod.Product.DoesNotExist:
        return HttpResponseRedirect('/manager/proudcts/')

    # Process Edit form
    form = EditPrductForm(initial=model_to_dict(product))
    if request.method=='POST':
        form = EditProductForm(request.POST)
        if form.is_valid():

            # Store captured form data to product we're editing
            product.name = form.cleaned_data.get('name')



            # Save changes
            product.save()

            # Redirect to users
            return HttpResponseRedirect('/manager/products/')

    template_vars = {
        'form': form,
        # 'user': user,
    }
    return dmp_render_to_response(request, 'products.edit.html', template_vars)


class EditProductForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, required=True)
    price = forms.CharField(label='Price', max_length=100, required=False)
    description = forms.CharField(label='Description', max_length=100, required=False)
    image = forms.CharField(label='Image', max_length=100, required=False)
    # Create form fields depending on which type of product you're working with
    if product.__class__.name == "Rental Product":
        purchase_date = forms.DateField(label='Purchase_date', required=False)
        status = forms.CharField(label='Status', max_length=100, required=False)
    elif product.__class.name == "Indivdual Product":
        create_date = forms.DateField(label='Creation Date', required=False)
        creator = forms.ModelChoiceField(label='Creator', required=False, queryset=amod.User.objects.all())
    else:
        quantity = forms.IntegerField(label='Quantity', required=False)



################################################
############### Delete a Product ###############
################################################
@view_function
def delete(request):
    '''Deletes a Product'''
    try:
        product = cmod.Product.objects.get(id=request.urlparams[0])
    except cmod.Product.DoesNotExist:
        return HttpResponseRedirect('/manager/products/')

    # Delete the event
    product.delete()

    # Redirect
    return HttpResponseRedirect('/manager/products/')
