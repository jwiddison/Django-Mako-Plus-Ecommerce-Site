from django.conf import settings
from django import forms
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response
from catalog import models as cmod
import datetime

#
# events Home Page
#

@view_function
def process_request(request):
    '''List the users in a table on the screen '''
    events = cmod.Event.objects.all().order_by('name')


    template_vars = {
      'events': events,
    }
    return dmp_render_to_response(request, 'events.html', template_vars)

################################################
########### Create a New event ##################
################################################

@view_function
def create(request):
    '''Create a New event'''
    # process the form
    form = CreateeventForm()
    if request.method == 'POST':   # if they've submitted the form
        form = CreateeventForm(request.POST) # Re-create the form with data in it
        if form.is_valid():  # Validate said form using validations specified in form object we created

            # create a temporary event object
            e = cmod.Event()

            # Fill event object with the data captured from the form
            e.name = form.cleaned_data.get('name')
            e.address = form.cleaned_data.get('address')
            e.city = form.cleaned_data.get('city')
            e.state = form.cleaned_data.get('state')
            e.zip_code = form.cleaned_data.get('zip_code')

            # Update database with event object
            e.save()

            # Redirect to confirmation page (change once login above is working)
            return HttpResponseRedirect('/manager/events/')

    # parameters from the email back to the browser just in case we need them later.
    template_vars = {
        'form': form,
    }
    return dmp_render_to_response(request, 'events.create.html', template_vars)

class CreateEventForm(forms.Form):
    name = forms.CharField(label='event Name', required=True, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Event Name'}))
    description = forms.CharField(label='Address Line 1', required=False, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Description'}))
    start_date = forms.DateField(label='Address Line 1', required=False, widget=forms.TextInput(attrs={'placeholder': 'Start Date'}))
    end_date = forms.DateField(label='Address Line 1', required=False, widget=forms.TextInput(attrs={'placeholder': 'End Date'}))
    venue = forms.CharField(label='Address Line 1', required=False, widget=forms.TextInput(attrs={'placeholder': 'Venue'}))

    # Make sure that the name for the event they're signing up with is unique.
    # def clean_name(self):
    #     event = self.cleaned_data.get('name')
    #     try:
    #         event = cmod.Event.objects.get(name=name)
    #         raise forms.ValidationError('This event Name is already taken')
    #     except cmod.Event.DoesNotExist:
    #         pass
    #     return name


################################################
################# Edit a event ##################
################################################

@view_function
def edit(request):
    '''Edits a event'''
    # Make sure that the ID number in the URL matches a event that actually exists
    try:
        event = cmod.Event.objects.get(id=request.urlparams[0])
    except cmod.Event.DoesNotExist:
        return HttpResponseRedirect('/manager/events/')

    # Process Edit form
    form = EditEventForm(initial=model_to_dict(event))
    if request.method=='POST':
        form = EditEventForm(request.POST)
        if form.is_valid():

            # Store captured form data to event we're editing
            event.name = form.cleaned_data.get('name')
            event.description = form.cleaned_data.get('description')
            event.start_date = form.cleaned_data.get('start_date')
            event.end_date = form.cleaned_data.get('end_date')
            event.venue = form.cleaned_data.get('venue')

            # Save changes
            event.save()

            # Redirect to events
            return HttpResponseRedirect('/manager/events/')

    template_vars = {
        'form': form,
        # 'event': event,
    }
    return dmp_render_to_response(request, 'events.edit.html', template_vars)


class EditEventForm(forms.Form):
    name = forms.CharField(label='Name', required=True, max_length=100)
    description = forms.CharField(label='Description', required=True, max_length=100)
    start_date = forms.DateField(label='Start Date', required=True)
    end_date = forms.DateField(label='End Date', required=True)
    venue = forms.CharField(label='Venue', required=True, max_length=100)



################################################
############### Delete a event #################
################################################

@view_function
def delete(request):
    '''Deletes a event'''
    try:
        event = cmod.Event.objects.get(id=request.urlparams[0])
    except cmod.Event.DoesNotExist:
        return HttpResponseRedirect('/manager/events/')

    # Delete the event
    event.delete()

    # Redirect
    return HttpResponseRedirect('/manager/events/')
