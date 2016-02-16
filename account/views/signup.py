from django.conf import settings
from django_mako_plus.controller import view_function
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django import forms
from .. import dmp_render, dmp_render_to_response
from account.models import User

@view_function
def process_request(request):

  # process the form
  form = SignupForm()
  if request.method == 'POST':   # if they've submitted the form
    form = SignupForm(request.POST) # Re-create the form with data in it
    if form.is_valid():  # Validate said form using validations specified in form object we created

        # create a temporary user object
        u = User()

        # Fill user object with the data captured from the form
        u.username = form.cleaned_data.get('username')
        u.first_name = form.cleaned_data.get('first_name')
        u.last_name = form.cleaned_data.get('last_name')
        u.email = form.cleaned_data.get('email')
        u.set_password(form.cleaned_data.get('password'))
        u.address1 = form.cleaned_data.get('address1')
        u.address2 = form.cleaned_data.get('address2')
        u.city = form.cleaned_data.get('city')
        u.state = form.cleaned_data.get('state')
        u.zip_code = form.cleaned_data.get('zip_code')
        u.phone_number = form.cleaned_data.get('phone_number')

        # Update database with user object
        u.save()

        # Login in the user that just signed up
        user = authenticate(username=u.username, password=form.cleaned_data.get('password'))
        login(request, user)

        # Redirect to confirmation page (change once login above is working)
        return HttpResponseRedirect('/homepage/index')

  # parameters from the email back to the browser just in case we need them later.
  template_vars = {
    'form': form,
  }
  return dmp_render_to_response(request, 'signup.html', template_vars)


# Create the form using Django's Form Class
class SignupForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(label='Enter Password', required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}))
    password2 = forms.CharField(label='Confirm Password', required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    first_name = forms.CharField(label='First Name', max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(label='Last Name', max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    email = forms.EmailField(label='Email Address', required=True, widget=forms.TextInput(attrs={'placeholder': 'Email Address'}))
    address1 = forms.CharField(label='Address Line 1', required=True, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Address Line 1'}))
    address2 = forms.CharField(label='Address Line 2', required=False, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Address Line 2'}))
    city = forms.CharField(label='City', required=True, widget=forms.TextInput(attrs={'placeholder': 'City'}))
    state = forms.CharField(label='State', required=True, widget=forms.TextInput(attrs={'placeholder': 'State'}))
    zip_code = forms.CharField(label='Zip Code', required=True, widget=forms.TextInput(attrs={'placeholder': 'Zip Code'}))
    phone_number = forms.CharField(label="Phone Number", required=True,widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))

    ## ----- CUSTOM VALIDATION METHODS ----- ##

    # Make sure that the username they're signing up with is unique.
    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            user = User.objects.get(username=username)
            raise forms.ValidationError('This username is already taken')
        except User.DoesNotExist as e: # Creates and "error" object
            pass # Do nothing because we don't want the username to exist, we're checking to make sure the one they're signing up with is unique
        return username

    # Make sure the two passwords are equal to each other
    def clean(self):
        if self.cleaned_data.get('password') != self.cleaned_data.get('password2'):
            raise forms.ValidationError("Your passwords don't match")
        return self.cleaned_data
