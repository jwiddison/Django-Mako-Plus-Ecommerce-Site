from django.conf import settings
from django import forms
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django_mako_plus.controller import view_function
from django.contrib.auth.decorators import permission_required
from .. import dmp_render, dmp_render_to_response
from catalog import models as cmod
import datetime



################################################################################################
########### Create a New area ##################################################################
################################################################################################
@view_function
@permission_required('catalog.add_area', login_url='/homepage/index/')
def create(request):
    '''Create a New area'''
    # process the form
    form = CreateAreaForm()
    if request.method == 'POST':   # if they've submitted the form
        form = CreateAreaForm(request.POST) # Re-create the form with data in it
        if form.is_valid():  # Validate said form using validations specified in form object we created

            # create a temporary area object
            a = cmod.Area()

            # Fill area object with the data captured from the form
            a.name = form.cleaned_data.get('name')
            a.description = form.cleaned_data.get('description')
            a.place_number = form.cleaned_data.get('place_number')
            a.event = form.cleaned_data.get('event')

            # Update database with area object
            a.save()

            # Redirect to confirmation page (change once login above is working)
            return HttpResponseRedirect('/manager/events/')

    # parameters from the email back to the browser just in case we need them later.
    template_vars = {
        'form': form,
    }
    return dmp_render_to_response(request, 'areas.create.html', template_vars)



class CreateAreaForm(forms.Form):
    name = forms.CharField(label='area Name', required=True, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'area Name'}))
    description = forms.CharField(label='Desctiption', required=False, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Description'}))
    place_number = forms.IntegerField(label='Place Number', required=False, widget=forms.TextInput(attrs={'placeholder': '10'}))
    event = forms.ModelChoiceField(label='Event', required=False, queryset=cmod.Event.objects.all())


################################################################################################
################# Edit an area #################################################################
################################################################################################
@view_function
@permission_required('catalog.change_area', login_url='/homepage/index/')
def edit(request):
    '''Edits a area'''
    # Make sure that the ID number in the URL matches a area that actually exists
    try:
        area = cmod.Area.objects.get(id=request.urlparams[0])
    except cmod.Area.DoesNotExist:
        return HttpResponseRedirect('/manager/events/')

    # Process Edit form
    form = EditAreaForm(initial=model_to_dict(area))
    if request.method=='POST':
        form = EditAreaForm(request.POST)
        if form.is_valid():

            # Store captured form data to area we're editing
            area.name = form.cleaned_data.get('name')
            area.description = form.cleaned_data.get('description')
            area.place_number = form.cleaned_data.get('place_number')
            area.event = form.cleaned_data.get('event')

            # Save changes
            area.save()

            # Redirect to areas
            return HttpResponseRedirect('/manager/events/')

    template_vars = {
        'form': form,
    }
    return dmp_render_to_response(request, 'areas.edit.html', template_vars)


class EditAreaForm(forms.Form):
    name = forms.CharField(label='Name', required=True, max_length=100)
    description = forms.CharField(label='Description', required=False, max_length=100)
    place_number = forms.IntegerField(label='Place Number', required=False)
    event = forms.ModelChoiceField(label='Event', required=False, queryset=cmod.Event.objects.all())



################################################################################################
############### Delete an area #################################################################
################################################################################################
@view_function
@permission_required('catalog.delete_area', login_url='/homepage/index/')
def delete(request):
    '''Deletes a area'''
    try:
        area = cmod.Area.objects.get(id=request.urlparams[0])
    except cmod.Area.DoesNotExist:
        return HttpResponseRedirect('/')

    # Delete the area
    area.delete()

    # Redirect
    return HttpResponseRedirect
