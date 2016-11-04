from django.conf import settings
from django_mako_plus import view_function
from django import forms
from django.http import HttpResponseRedirect
from .. import dmp_render_to_string, dmp_render
from account.models import User


@view_function
def process_request(request):
    # Make sure user is logged in
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/account/login/')


    # process the form
    form = EditForm(initial={
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'email': request.user.email,
        'address1': request.user.address1,
        'address2': request.user.address2,
        'city': request.user.city,
        'state': request.user.state,
        'zip_code': request.user.zip_code,
        'phone_number': request.user.phone_number,
    })

    if request.method == 'POST':
        form = EditForm(request.POST)
        if form.is_valid():

            # Get currently logged in user
            u = request.user

            # Fill user object with the data captured from the form (changed or not)
            u.first_name = form.cleaned_data.get('first_name')
            u.last_name = form.cleaned_data.get('last_name')
            u.email = form.cleaned_data.get('email')
            u.address1 = form.cleaned_data.get('address1')
            u.address2 = form.cleaned_data.get('address2')
            u.city = form.cleaned_data.get('city')
            u.state = form.cleaned_data.get('state')
            u.zip_code = form.cleaned_data.get('zip_code')
            u.phone_number = form.cleaned_data.get('phone_number')

            # Update user information to user object
            u.save()

            # Redirect to confirmation page
            return HttpResponseRedirect('/account/index')

    # parameters from the email back to the browser just in case we need them later.
    template_vars = {
        'form': form,
    }
    return dmp_render(request, 'edit.html', template_vars)

# DON'T LET THE USER CHANGE USERNAME OR PASSWORD #

class EditForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100, required=True)
    last_name = forms.CharField(label='Last Name', max_length=100, required=True)
    email = forms.EmailField(label='Email Address', required=True)
    address1 = forms.CharField(label='Address Line 1', required=True, max_length=100)
    address2 = forms.CharField(label='Address Line 2', required=False, max_length=100)
    city = forms.CharField(label='City', required=True)
    state = forms.CharField(label='State', required=True)
    zip_code = forms.CharField(label='Zip Code', required=True)
    phone_number = forms.CharField(label="Phone Number", required=True)
