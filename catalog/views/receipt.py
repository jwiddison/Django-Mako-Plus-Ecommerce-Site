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


    # Send the receipt as an email
    subject = 'CHFSales.com Order Confirmation Receipt'
    from_email = settings.EMAIL_HOST_USER
    to = 'jordan.widdison@gmail.com'
    text_content = 'Email Confirmation of CHFSales.com Order'
    # html_content = dmp_render(request, '/catalog/receipt/%s' % (str(sale.id)))
    html_content = '''
        <html>
            <body>
                <h3>CHFSales.com Order Receipt</h3>
                <hr />
                <br />
                <p>Thank you for your purchase!  Please keep a copy of this recipt for your records.</p>
                <h4>Ship To:</h4>
                <ul style="list-style:none">
                <li>''' + sale.ShipName + '''</li>
                <li>''' + sale.ShipAddress + '''</li>
                <li>''' + sale.ShipCity + '''</li>
                <li>''' + sale.ShipState + '''</li>
                <li>''' + sale.ShipZipCode + '''</li>
                </ul>
                <h4>Tracking Number:</h4>
                <p>''' + sale.TrackingNumber + '''</p>
                <h4>Order Total:</h4>
                <p>$''' + str(sale.TotalPrice) + '''</p>
                <h4>Thank you for your order!</h4>
            </body>
        </html>
        '''
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


    # Send Sale to the template
    template_vars['sale'] = sale
    template_vars['saleitems'] = sale.get_saleitems()
    return dmp_render_to_response(request, 'receipt.html', template_vars)
