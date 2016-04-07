from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response
from catalog import models as cmod
from . import initialize_template_vars
from django.core.mail import send_mail, EmailMultiAlternatives


@view_function
def process_request(request):
    template_vars = initialize_template_vars(request)

    # Get the sale off the url
    try:
        sale = cmod.Sale.objects.get(id=request.urlparams[0])
    except cmod.Sale.DoesNotExist:
        return HttpResponseRedirect('/catalog/index/')


    #message = 'test email'
    # subject = 'CHFSales.com Order Confirmation Receipt'
    # from_email = 'orders@chfsales.com'
    # to = 'jordan.widdison@gmail.com'
    # text_content = 'Email Confirmation of CHFSales.com Order'
    # html_content = dmp_render(request, '/catalog/receipt/%s/' % (sale.id))
    # msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    # msg.attach_alternative(html_content, "text/html")
    # msg.send()
    # send_mail('CHFSales.com Order Confirmation Receipt', message, 'orders@chfsales.com', ['jordan.widdison@gmail.com'])

    saleitems = sale.get_saleitems()
    # print(saleitems)

    # Send Sale to the template
    template_vars['sale'] = sale
    template_vars['saleitems'] = saleitems
    return dmp_render_to_response(request, 'receipt.html', template_vars)
