from django.conf import settings
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response
from account.models import User

@view_function
def process_request(request):

    # If already logged in, go to the account area (Use in navbar too)
    if request.user.is_authenticated():
        return HttpResponseRedirect('/homepage/index/')

    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Log the User in
            login(request, form.user) # Can use form.user because it was added to 'self' in the clean method
            # Redirect to Home Page using AJAX
            return HttpResponse('''
                <script>
                    window.location.href = '/homepage/index/';
                </script>
            ''')

    template_vars = {
        'form': form,
    }
    return dmp_render_to_response(request, 'login.html', template_vars)


# Create the form using Django's Form Class
class LoginForm(forms.Form):
    username = forms.CharField(label='Username', required=True, max_length=50)
    password = forms.CharField(label='Password', required=True, widget=forms.PasswordInput())

    # This method just authenticates the user, but doesn't log them in yet.
    def clean(self):
        user = authenticate(username=self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))
        if user == None:
            raise forms.ValidationError('This username and password does not match our records.')
        self.user = user
        return self.cleaned_data

    # Just FYI, Normal way to pull any model out of the database.  Can't do this because our password is hashed.
    # user = User.objects.get(username=self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))
