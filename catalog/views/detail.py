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

    try:
        p = cmod.Product.objects.get(id=request.urlparams[0])
    except cmod.Proudct.DoesNotExist:
        return HttpResponseRedirect('/catalog/index/')

    # Add to Last5 Viewed
    request.shopping_cart.item_viewed(p)
    #
    # form = OrderForm(initial={'quantity':1})
    # form.product = p
    # if request.method == 'POST':
    #     form = OrderForm(request.POST)
    #     form.request = request
    #     form.product = p
    #     if form.is_valid():
    #         request.shopping_cart.add_item(p, form.cleaned_data.get('quantity'))
    #         return HttpResponseRedirect('/catalog/cart/')

    template_vars['p'] = p
    # template_vars['form'] = form
    return dmp_render_to_response(request, 'detail.html', template_vars)


# Form for submitting quantity to cart
# class OrderForm(forms.Form):
#     quantity = forms.IntegerField(label='Quantity', required=True, min_value=1, max_value=100, widget=forms.NumberInput(attrs={'class': 'form-control', 'id': 'add_form'}))
#     default_data = {'quantity': '1'}
#     def clean_quantity(self):
#         qty = self.cleaned_data.get('quantity')
#         try:
#             self.request.shopping_cart.check_availability(self.product, qty)
#         except ValueError:
#             raise forms.ValidationError('Desired quantity not available.  Please decrease the quantity requested')
#         return self.cleaned_data['quantity']

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
