from django.conf import settings
from django_mako_plus import view_function
from .. import dmp_render_to_string, dmp_render
from django.core.mail import send_mail, EmailMultiAlternatives
from django import forms
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect



@view_function
def process_request(request):

    sentmessage = ''

    form = EmailForm()
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():

            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            message = form.cleaned_data.get('message')

            try:
                send_mail(
                    'Email from CHFSales.com from %s' % (name),
                    'Here is your email:/nName: %s/nPhone: %s/nMessage: %s' % (name, phone, message),
                    'orders@chfsales.com',
                    ['jordan.widdison@gmail.com'],
                    fail_silently=False,
                )

                sentmessage = 'Thank you for your email.  Someone from CHFSales will be in touch with you soon.'
            except:
                sentmessage = 'There was a problem with your email.  Please try again later.'

            # return HttpResponseRedirect('/homepage/contact')

    ## parameters from the email back to the browser just in case we need them later.
    template_vars = {
        'form': form,
        'sentmessage': sentmessage,
    }
    return dmp_render(request, 'contact.html', template_vars)

class EmailForm(forms.Form):
    name = forms.CharField(label='Name', required=True, widget=forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control'}))
    email = forms.EmailField(label='Email', required=True, widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))
    phone = forms.CharField(label='Phone', required=True, widget=forms.TextInput(attrs={'placeholder': 'Phone', 'class': 'form-control'}))
    message = forms.CharField(label='Message', required=True, widget=forms.TextInput(attrs={'placeholder': 'Message', 'class': 'form-control'}))
