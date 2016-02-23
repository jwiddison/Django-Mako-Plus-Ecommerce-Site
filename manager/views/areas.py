from django import forms
from django.conf import settings
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

    # Create temporary event
    # area = cmod.Area.objects.get(id=request.urlparams[0])
    # event = area.event
    #url = '/manager/events.edit/' + str(event.id)

    form = CreateAreaForm()
    if request.method == 'POST':
        form = CreateAreaForm(request.POST)
        if form.is_valid():
            a = cmod.Area()
            a.name = form.cleaned_data.get('name')
            a.description = form.cleaned_data.get('description')
            a.place_number = form.cleaned_data.get('place_number')
            a.event = form.cleaned_data.get('event')
            a.save()
            url = '/manager/events.edit/' + str(a.event.id)
            return HttpResponseRedirect(url)

    template_vars = {
        'form': form,
    }
    return dmp_render_to_response(request, 'areas.create.html', template_vars)

class CreateAreaForm(forms.Form):
    name = forms.CharField(label='area Name', required=True, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'area Name'}))
    description = forms.CharField(label='Desctiption', required=False, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Description'}))
    place_number = forms.IntegerField(label='Place Number', required=False, widget=forms.TextInput(attrs={'placeholder': '10'}))
    event = forms.ModelChoiceField(label='Event', required=True, queryset=cmod.Event.objects.all())
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

    # Get event id
    event = area.event
    url = '/manager/events.edit/' + str(event.id)

    form = EditAreaForm(initial=model_to_dict(area))
    if request.method=='POST':
        form = EditAreaForm(request.POST)
        if form.is_valid():
            area.name = form.cleaned_data.get('name')
            area.description = form.cleaned_data.get('description')
            area.place_number = form.cleaned_data.get('place_number')
            area.save()
            return HttpResponseRedirect(url)

    template_vars = {
        'form': form,
        'event': event,
    }
    return dmp_render_to_response(request, 'areas.edit.html', template_vars)

class EditAreaForm(forms.Form):
    name = forms.CharField(label='Name', required=True, max_length=100)
    description = forms.CharField(label='Description', required=False, max_length=100)
    place_number = forms.IntegerField(label='Place Number', required=False)

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
        return HttpResponseRedirect('/manager/events/')

    event = area.event
    url = '/manager/events.edit/' + str(event.id)


    # Delete the area
    area.delete()

    # Redirect
    return HttpResponseRedirect(url)
