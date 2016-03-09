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

################################################
############### Products Homepage ##############
################################################
@view_function
@permission_required('catalog.change_product', login_url='/homepage/index/')
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
@permission_required('catalog.add_product', login_url='/homepage/index')
def create(request):
    '''Create a New Product'''
    # process the form
    form = CreateProductForm()
    if request.method == 'POST':   # if they've submitted the form
        form = CreateProductForm(request.POST) # Re-create the form with data in it
        if form.is_valid():  # Validate said form using validations specified in form object we created

            #Check the type of product and save attributes accordingly
            if form.cleaned_data.get('product_type') == 'RentalProduct':
                p = cmod.RentalProduct()
                p.purchase_date = form.cleaned_data.get('purchase_date')
                p.status = form.cleaned_data.get('status')
            elif form.cleaned_data.get('product_type') == 'IndividualProduct':
                p = cmod.IndividualProduct()
                p.create_date = form.cleaned_data.get('create_date')
                p.creator = form.cleaned_data.get('creator')
            elif form.cleaned_data.get('product_type') == 'BulkProduct':
                p = cmod.BulkProduct()
                p.quantity = form.cleaned_data.get('quantity')

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
    PRODUCT_CHOICE_LIST =(
		('RentalProduct', 'Rental Product'),
		('IndividualProduct', 'Individual Product'),
		('BulkProduct', 'Bulk Product'),
    )
    product_type = forms.ChoiceField(label="Product Type", required=False, choices=PRODUCT_CHOICE_LIST)
    name = forms.CharField(label='Product Name', required=True, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Product Name'}))
    price = forms.CharField(label='Price', required=False, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Price'}))
    description = forms.CharField(label='Description', required=False, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Description'}))
    image = forms.CharField(label='Image', required=False, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Image'}))
    # Create form fields depending on which type of product you're working with
    purchase_date = forms.DateField(label='Purchase_date', required=False, widget=forms.TextInput(attrs={'placeholder': '2000-01-01'}))
    status = forms.CharField(label='Status', max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder': 'Availability Status'}))
    create_date = forms.DateField(label='Creation Date', required=False, widget=forms.TextInput(attrs={'placeholder': '2000-01-01'}))
    creator = forms.ModelChoiceField(label='Creator', required=False, queryset=amod.User.objects.all())
    quantity = forms.IntegerField(label='Quantity', required=False, widget=forms.TextInput(attrs={'placeholder': 0}))


################################################
################# Edit a Product ###############
################################################
@view_function
@permission_required('catalog.change_product', login_url='/homepage/index/')
def edit(request):
    '''Edits a Product'''
    # Make sure that the ID number in the URL matches a user that actually exists
    try:
        product = cmod.Product.objects.get(id=request.urlparams[0])
    except cmod.Product.DoesNotExist:
        return HttpResponseRedirect('/manager/products/')

    # Process Edit form
    form = EditProductForm(initial=model_to_dict(product))
    if request.method=='POST':
        form = EditProductForm(request.POST)
        if form.is_valid():

            # Store captured form data to product we're editing
            product.name = form.cleaned_data.get('name')
            product.price = form.cleaned_data.get('price')
            product.description = form.cleaned_data.get('description')
            product.image = form.cleaned_data.get('image')
            if product.__class__.className == 'Rental Product':
                product.purchase_date = form.cleaned_data.get('purchase_date')
                product.status = form.cleaned_data.get('status')
            elif product.__class__.className == 'Individual Product':
                product.create_date = form.cleaned_data.get('create_date')
                product.creator = form.cleaned_data.get('creator')
            elif product.__class__.className == 'Bulk Product':
                product.quantity = form.cleaned_data.get('quantity')

            # Save changes
            product.save()

            # Redirect to users
            return HttpResponseRedirect('/manager/products/')

    template_vars = {
        'form': form,
        'product_type': product.__class__.className

    }
    return dmp_render_to_response(request, 'products.edit.html', template_vars)


class EditProductForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, required=True)
    price = forms.CharField(label='Price', max_length=100, required=False)
    description = forms.CharField(label='Description', max_length=100, required=False)
    image = forms.CharField(label='Image', max_length=100, required=False)
    # Create form fields depending on which type of product you're working with
    purchase_date = forms.DateField(label='Purchase_date', required=False)
    status = forms.ChoiceField(label='Status', required=False, choices=cmod.RENTAL_STATUS_CHOICES)
    create_date = forms.DateField(label='Creation Date', required=False)
    creator = forms.ModelChoiceField(label='Creator', required=False, queryset=amod.User.objects.all())
    quantity = forms.IntegerField(label='Quantity', required=False)



################################################
############### Delete a Product ###############
################################################
@view_function
@permission_required('catalog.delete_product', login_url='/homepage/index/')
def delete(request):
    '''Deletes a Product'''
    try:
        product = cmod.Product.objects.get(id=request.urlparams[0])
    except cmod.Product.DoesNotExist:
        return Http404()

    # Delete the event
    product.delete()

    # Redirect
    return HttpResponseRedirect('/manager/products/')

################################################
############### Ajax  ##########################
################################################
@view_function
@permission_required('catalog.change_product', login_url='/homepage/index/')
def get_quantity(request):
   try:
       product = cmod.Product.objects.get(id=request.urlparams[0])
   except cmod.Product.DoesNotExist:
       return Http404()
   return HttpResponse(product.quantity)
