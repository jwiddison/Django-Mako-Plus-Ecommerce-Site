from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response
from catalog import models as cmod
from . import initialize_template_vars
from django.core.mail import send_mail


@view_function
def process_request(request):
    template_vars = initialize_template_vars(request)

    # Get the sale off the url
    try:
        sale = cmod.Sale.objects.get(id=request.urlparams[0])
    except cmod.Product.DoesNotExist:
        return HttpResponseRedirect('/catalog/index/')

    send_mail(
        'CHFSales.com Order Confirmation', # Subject
        'Testing the Message', # Message
        'orders@chfsales.com', # From address
        ['jordan.widdison@gmail.com'], # To address
        fail_silenty=False
    )

    saleitems = sale.get_saleitems()
    print(saleitems)

    # Send Sale to the template
    template_vars['sale'] = sale
    template_vars['saleitems'] = saleitems
    return dmp_render_to_response(request, 'receipt.html', template_vars)
