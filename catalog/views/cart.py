from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response
from catalog import models as cmod
from . import initialize_template_vars
from Colonial_Heritage_Foundation.customform import CustomForm


@view_function
def process_request(request):
    # Initialize Template Vars
    template_vars = initialize_template_vars(request)
    return dmp_render_to_response(request, 'cart.html', template_vars)

@view_function
def clear(request):
    request.shopping_cart.clear_items()
    return HttpResponseRedirect('/catalog/cart/')

@view_function
def remove(request):
    p = cmod.Product.objects.get(id=request.urlparams[0])
    request.shopping_cart.remove_item(p)
    return HttpResponseRedirect('/catalog/cart/')

## FOR AJAX SHOPPING CART
@view_function
def add(request):
    try:
        p = cmod.Product.objects.get(id=request.urlparams[0])
    except cmod.Product.DoesNotExist:
        return Http404()

    template_vars = initialize_template_vars(request)

    form = AddForm(request, initial={'quantity':1}, extra={'product':p})
    if request.method == 'POST':
        form = AddForm(request, request.POST, extra={'product':p})
        if form.is_valid():
            try:
                request.shopping_cart.add_item(p, form.cleaned_data['quantity'])
            except ValueError as e:
                form.add_error('quantity', str(e))

    template_vars['form'] = form
    template_vars['p'] = p
    return dmp_render_to_response(request, 'cart.add.html', template_vars)

# Form for submitting quantity to cart
class AddForm(CustomForm):
    quantity = forms.IntegerField(label='', required=False, min_value=1, max_value=100, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    def clean_quantity(self):
        ''' Ensures we have enough of this product '''
        try:
            self.request.shopping_cart.check_availability(self.extra['product'], self.cleaned_data.get('quantity'))
        except ValueError as e:
            raise forms.ValidationError(str(e))
        return self.cleaned_data['quantity']
