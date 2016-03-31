from django.conf import settings
from django import forms
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django_mako_plus.controller import view_function
from django.contrib.auth.models import Permission, Group
from django.contrib.auth.decorators import permission_required
from .. import dmp_render, dmp_render_to_response
from account import models as amod
import datetime


################################################################################################
############### Users Homepage #################################################################
################################################################################################
@view_function
@permission_required('account.change_user', login_url='/homepage/index/')
def process_request(request):
    '''List the users in a table on the screen '''
    users = amod.User.objects.all().order_by('username')

    template_vars = {
      'users': users,
    }
    return dmp_render_to_response(request, 'users.html', template_vars)

################################################################################################
########### Create a New User ##################################################################
################################################################################################
@view_function
@permission_required('account.add_user', login_url='/homepage/index/')
def create(request):
    '''Create a New User'''
    # process the form
    form = CreateForm()
    if request.method == 'POST':   # if they've submitted the form
        form = CreateForm(request.POST) # Re-create the form with data in it
        if form.is_valid():  # Validate said form using validations specified in form object we created

            # create a temporary user object
            u = amod.User()

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
            u.birth = form.cleaned_data.get('birth')

            # required to save twice, so this saves the above form fields.
            u.save()

            u.groups.clear()
            u.user_permissions.clear()
            for group in form.cleaned_data['groups']:
                u.groups.add(group)
            for permission in form.cleaned_data['user_permissions']:
                u.user_permissions.add(permission)
            # This saves the groups and permissions
            u.save()

            # Redirect to confirmation page (change once login above is working)
            return HttpResponseRedirect('/manager/users/')

    # parameters from the email back to the browser just in case we need them later.
    template_vars = {
      'form': form,
    }
    return dmp_render_to_response(request, 'users.create.html', template_vars)

class CreateForm(forms.Form):
    username = forms.CharField(label='Username', required=True, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))
    password = forms.CharField(label='Password', required=True, widget=forms.TextInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))
    first_name = forms.CharField(label='First Name', required=False, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}))
    last_name = forms.CharField(label='Last Name', required=False, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}))
    birth = forms.DateField(label='Birth Date', required=True, input_formats=['%Y-%m-%d'], widget=forms.TextInput(attrs={'placeholder': '1980-01-01', 'class': 'form-control'}))
    email = forms.EmailField(label='Email Address', required=False, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Email Address', 'class': 'form-control'}))
    address1 = forms.CharField(label='Address Line 1', required=False, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Address Line 1', 'class': 'form-control'}))
    address2 = forms.CharField(label='Address Line 2', required=False, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Address Line 2', 'class': 'form-control'}))
    city = forms.CharField(label='City', required=False, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'City', 'class': 'form-control'}))
    state = forms.CharField(label='State', required=False, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'State', 'class': 'form-control'}))
    zip_code = forms.CharField(label='Zip Code', required=False, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Zip Code', 'class': 'form-control'}))
    phone_number = forms.CharField(label="Phone Number", required=False, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Phone Number', 'class': 'form-control'}))
    groups = forms.ModelMultipleChoiceField(label='Groups', required=False, queryset=Group.objects.all(), widget=forms.CheckboxSelectMultiple())
    user_permissions = forms.ModelMultipleChoiceField(label='Permissions', required=False, queryset=Permission.objects.all(), widget=forms.CheckboxSelectMultiple)
    ## ----- CUSTOM VALIDATIONS ------ ##

    # Make sure that the username they're signing up with is unique.
    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            user = amod.User.objects.get(username=username)
            raise forms.ValidationError('This username is already taken')
        except amod.User.DoesNotExist:
            pass
        return username


################################################################################################
################# Edit a User ##################################################################
################################################################################################
@view_function
@permission_required('account.change_user', login_url='/homepage/index/')
def edit(request):
    '''Edits a User'''
    # Make sure that the ID number in the URL matches a user that actually exists
    try:
        user = amod.User.objects.get(id=request.urlparams[0])
    except amod.User.DoesNotExist:
        return HttpResponseRedirect('/manager/users/')

    # Process Edit form
    form = EditForm(initial=model_to_dict(user))
    if request.method=='POST':
        form = EditForm(request.POST)
        form.user = user
        if form.is_valid():

            # Store captured form data to user we're editing
            user.username = form.cleaned_data.get('username')
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.email = form.cleaned_data.get('email')
            user.address1 = form.cleaned_data.get('address1')
            user.address2 = form.cleaned_data.get('address2')
            user.city = form.cleaned_data.get('city')
            user.state = form.cleaned_data.get('state')
            user.zip_code = form.cleaned_data.get('zip_code')
            user.phone_number = form.cleaned_data.get('phone_number')
            user.birth = form.cleaned_data.get('birth')

            # Save changes first time
            user.save()

            # Make changes to groups/permissions
            user.groups.clear()
            user.user_permissions.clear()
            for group in form.cleaned_data['groups']:
                user.groups.add(group)
            for permission in form.cleaned_data['user_permissions']:
                user.user_permissions.add(permission)
            # This saves the groups and permissions
            user.save()

            # Redirect to users
            return HttpResponseRedirect('/manager/users/')

    template_vars = {
        'form': form,
    }
    return dmp_render_to_response(request, 'users.edit.html', template_vars)


class EditForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='First Name', max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Last Name', max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    birth = forms.DateField(label='Birth Date', required=False, input_formats=['%Y-%m-%d'], widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email Address', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address1 = forms.CharField(label='Address Line 1', required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address2 = forms.CharField(label='Address Line 2', required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.CharField(label='City', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    state = forms.CharField(label='State', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    zip_code = forms.CharField(label='Zip Code', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(label="Phone Number", required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    groups = forms.ModelMultipleChoiceField(label='Groups', required=False, queryset=Group.objects.all(), widget=forms.CheckboxSelectMultiple)
    user_permissions = forms.ModelMultipleChoiceField(label='Permissions', required=False, queryset=Permission.objects.all(), widget=forms.CheckboxSelectMultiple)

    # Make sure that the username, if you change it, isn't already taken.
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if amod.User.objects.filter(username=username).exclude(id=self.user.id).count() > 0:
            raise forms.ValidationError('This username is already taken')
        return username


################################################################################################
############### Delete a User ##################################################################
################################################################################################
@view_function
@permission_required('account.delete_user', login_url='/homepage/index/')
def delete(request):
    '''Deletes a User'''
    try:
        user = amod.User.objects.get(id=request.urlparams[0])
    except amod.User.DoesNotExist:
        return HttpResponseRedirect('/manager/users/')

    # Delete the user
    user.delete()

    # Redirect
    return HttpResponseRedirect('/manager/users/')


################################################################################################
############## Change Password #################################################################
################################################################################################
@view_function
@permission_required('account.change_user', login_url='/homepage/index/')
def password(request):
    '''Change a user password'''
    try:
        user = amod.User.objects.get(id=request.urlparams[0])
    except amod.User.DoesNotExist:
        raise HttpResponse('/manager/users/')

    form = PasswordForm()
    if request.method == 'POST':
        form = PasswordForm(request.POST)
        if form.is_valid():

            # Save the password to that user
            user.set_password(form.cleaned_data.get('new_password'))
            # Save changes to the user
            user.save()

            # Redirect to confirmation page (change this later)
            return HttpResponseRedirect('/manager/users/')

    # parameters from the email back to the browser just in case we need them later.
    template_vars = {
        'form': form,
    }
    return dmp_render_to_response(request, 'users.password.html', template_vars)


class PasswordForm(forms.Form):
    new_password = forms.CharField(label='New Password', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(label='Confirm New Password', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    # Make sure the two passwords are equal to each other
    def clean(self):
        if self.cleaned_data.get('new_password') != self.cleaned_data.get('new_password2'):
            raise forms.ValidationError("Your passwords don't match")
        return self.cleaned_data
