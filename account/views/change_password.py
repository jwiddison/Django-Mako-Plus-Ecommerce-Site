from django.conf import settings
from django.contrib.auth import authenticate, login
from django_mako_plus.controller import view_function
from django import forms
from django.http import HttpResponseRedirect
from .. import dmp_render, dmp_render_to_response
from account.models import User

@view_function
def process_request(request):
    # Make sure user is logged in
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/account/login/')

    form = ChangePasswordForm()
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        form.user = request.user # Add user to the form object so you can use it below
        if form.is_valid():
            # Get currently logged-in user
            u = request.user
            # Save the password to that user
            u.set_password(form.cleaned_data.get('new_password'))
            # Save changes to the user
            u.save()
            # Log in new user
            user = authenticate(username=u.username, password=form.cleaned_data.get('new_password'))
            login(request, user)
            # Redirect to confirmation page (change this later)
            return HttpResponseRedirect('/account/index/')

    # parameters from the email back to the browser just in case we need them later.
    template_vars = {
        'form': form,
    }
    return dmp_render_to_response(request, 'change_password.html', template_vars)


# Create the form using Django's Form Class
class ChangePasswordForm(forms.Form):
    currentpassword = forms.CharField(label='Current Password', required=True, widget=forms.PasswordInput())
    new_password = forms.CharField(label='New Password', required=True, widget=forms.PasswordInput())
    new_password2 = forms.CharField(label='Confirm New Password', required=True, widget=forms.PasswordInput())

    # Make sure the password they entered is the same as the password for the currently logged in user
    def clean_currentpassword(self):
        if not self.user.check_password(self.cleaned_data.get('currentpassword')):
            raise forms.ValidationError("You entered the current password incorrectly")
        return self.cleaned_data.get('currentpassword')

    # Make sure the two passwords are equal to each other
    def clean(self):
        if self.cleaned_data.get('new_password') != self.cleaned_data.get('new_password2'):
            raise forms.ValidationError("Your passwords don't match")
        return self.cleaned_data
