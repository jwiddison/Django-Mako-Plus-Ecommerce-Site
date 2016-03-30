from django.conf import settings
from django import forms
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response
from catalog import models as cmod
from . import initialize_template_vars

@view_function
def process_request(request):
    # Initialize Template vars
    template_vars = initialize_template_vars(request)

    # Get the product that we're working with and send it to template
    p = cmod.Product.objects.get(id=request.urlparams[0])

    request.shopping_cart.item_viewed(p)

    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            request.shopping_cart.add_item(p, form.cleaned_data.get('quantity'))
            print(request.shopping_cart.cart)
            return HttpResponseRedirect('/catalog/cart/')


    template_vars['p'] = p
    template_vars['form'] = form
    return dmp_render_to_response(request, 'detail.html', template_vars)

### Carousel Method
@view_function
def carousel(request):

    # I'm sending p so I have access to the name for the modal title.
    p = cmod.Product.objects.get(id=request.urlparams[0])

    template_vars = {
        'p': p,
        'p_images': cmod.ProductImage.objects.all().filter(product=p),
    }
    return dmp_render_to_response(request, 'detail.carousel.html', template_vars)

# Form for submitting quantity to cart
class OrderForm(forms.Form):
    quantity = forms.IntegerField(label='Quantity', widget=forms.NumberInput(attrs={'placeholder': '1', 'class': 'form-control'}))

    def clean_quantity(self):
        if self.cleaned_data.get('quantity') < 0:
            raise forms.ValidationError('Please enter a positive number for quantity')
