from django.conf import settings
from django import forms
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django_mako_plus.controller import view_function
from django.contrib.auth.decorators import permission_required
from .. import dmp_render, dmp_render_to_response
from catalog import models as cmod
import datetime

#
# Venues Home Page
#
@view_function
@permission_required('catalog.change_venue', login_url='/homepage/index/')
def process_request(request):
    '''List the venues in a table on the screen '''
    venues = cmod.Venue.objects.all().order_by('name')


    template_vars = {
      'venues': venues,
    }
    return dmp_render_to_response(request, 'venues.html', template_vars)


################################################
########### Create a New venue ##################
################################################
@view_function
@permission_required('catalog.add_venue', login_url='/homepage/index/')
def create(request):
    '''Create a New Venue'''
    # process the form
    form = CreateVenueForm()
    if request.method == 'POST':   # if they've submitted the form
        form = CreateVenueForm(request.POST) # Re-create the form with data in it
        if form.is_valid():  # Validate said form using validations specified in form object we created

            # create a temporary venue object
            v = cmod.Venue()

            # Fill venue object with the data captured from the form
            v.name = form.cleaned_data.get('name')
            v.address = form.cleaned_data.get('address')
            v.city = form.cleaned_data.get('city')
            v.state = form.cleaned_data.get('state')
            v.zip_code = form.cleaned_data.get('zip_code')

            # Update database with venue object
            v.save()

            # Redirect to confirmation page (change once login above is working)
            return HttpResponseRedirect('/manager/venues/')

    # parameters from the email back to the browser just in case we need them later.
    template_vars = {
        'form': form,
    }
    return dmp_render_to_response(request, 'venues.create.html', template_vars)

class CreateVenueForm(forms.Form):
    name = forms.CharField(label='Venue Name', required=True, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Venue Name'}))
    address = forms.CharField(label='Address Line 1', required=False, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Address'}))
    city = forms.CharField(label='City', required=False, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'City'}))
    state = forms.CharField(label='State', required=False, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'State'}))
    zip_code = forms.CharField(label='Zip Code', required=False, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Zip Code'}))

    # Make sure that the name for the venue they're signing up with is unique.
    # def clean_name(self):
    #     venue = self.cleaned_data.get('name')
    #     try:
    #         venue = cmod.Venue.objects.get(name=name)
    #         raise forms.ValidationError('This Venue Name is already taken')
    #     except cmod.Venue.DoesNotExist:
    #         pass
    #     return name


################################################
################# Edit a venue ##################
################################################
@view_function
@permission_required('catalog.change_venue', login_url='/homepage/index/')
def edit(request):
    '''Edits a venue'''
    # Make sure that the ID number in the URL matches a venue that actually exists
    try:
        venue = cmod.Venue.objects.get(id=request.urlparams[0])
    except cmod.venue.DoesNotExist:
        return HttpResponseRedirect('/manager/venues/')

    # Process Edit form
    form = EditVenueForm(initial=model_to_dict(venue))
    if request.method=='POST':
        form = EditVenueForm(request.POST)
        if form.is_valid():

            # Store captured form data to venue we're editing
            venue.name = form.cleaned_data.get('name')
            venue.address = form.cleaned_data.get('address')
            venue.city = form.cleaned_data.get('city')
            venue.state = form.cleaned_data.get('state')
            venue.zip_code = form.cleaned_data.get('zip_code')

            # Save changes
            venue.save()

            # Redirect to venues
            return HttpResponseRedirect('/manager/venues/')

    template_vars = {
        'form': form,
        # 'venue': venue,
    }
    return dmp_render_to_response(request, 'venues.edit.html', template_vars)


class EditVenueForm(forms.Form):
    name = forms.CharField(label='Name', required=True, max_length=100)
    address = forms.CharField(label='Address', required=False, max_length=100)
    city = forms.CharField(label='City', required=False, max_length=100)
    state = forms.CharField(label='State', required=False, max_length=100)
    zip_code = forms.CharField(label='Zip Code', required=False, max_length=100)


################################################
############### Delete a Venue #################
################################################
@view_function
@permission_required('catalog.delete_venue', login_url='/homepage/index/')
def delete(request):
    '''Deletes a Venue'''
    try:
        venue = cmod.Venue.objects.get(id=request.urlparams[0])
    except cmod.Venue.DoesNotExist:
        return HttpResponseRedirect('/manager/venues/')

    # Delete the venue
    venue.delete()

    # Redirect
    return HttpResponseRedirect('/manager/venues/')
