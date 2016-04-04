from django.conf import settings
from django import forms
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django_mako_plus.controller import view_function
from django.contrib.auth.decorators import permission_required
from .. import dmp_render, dmp_render_to_response
from catalog import models as cmod
from account import models as amod
import datetime

################################################
############### categorys Homepage ##############
################################################
@view_function
@permission_required('catalog.change_category', login_url='/homepage/index/')
def process_request(request):
    '''List the users in a table on the screen '''
    categories = cmod.Category.objects.all().order_by('name')

    template_vars = {
      'categories': categories,
    }
    return dmp_render_to_response(request, 'categories.html', template_vars)



################################################
############### Create a Category ##############
################################################
@view_function
@permission_required('catalog.add_category', login_url='/homepage/index')
def create(request):
    '''Create a New category'''
    # process the form
    form = CreatecategoryForm()
    if request.method == 'POST':
        form = CreatecategoryForm(request.POST)
        if form.is_valid():

            p.name = form.cleaned_data.get('name')
            p.description = form.cleaned_data.get('description')
            p.save()

            return HttpResponseRedirect('/manager/categories/')

    template_vars = {
      'form': form,
    }
    return dmp_render_to_response(request, 'categories.create.html', template_vars)

class CreateCategoryForm(forms.Form):
    name = forms.CharField(label='category Name', required=True, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'category Name'}))
    description = forms.CharField(label='Description', required=False, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Description'}))


################################################
################# Edit a category ###############
################################################
@view_function
@permission_required('catalog.change_category', login_url='/homepage/index/')
def edit(request):
    '''Edits a category'''
    try:
        c = cmod.Category.objects.get(id=request.urlparams[0])
    except cmod.category.DoesNotExist:
        return HttpResponseRedirect('/manager/categories/')

    form = EditCategoryForm(initial=model_to_dict(c))
    if request.method=='POST':
        form = EditCategoryForm(request.POST)
        if form.is_valid():

            # Store captured form data to category we're editing
            category.name = form.cleaned_data.get('name')
            category.description = form.cleaned_data.get('description')

            # Save changes
            category.save()

            # Redirect to users
            return HttpResponseRedirect('/manager/categories/')

    template_vars = {
        'form': form,
    }
    return dmp_render_to_response(request, 'categories.edit.html', template_vars)


class EditCategoryForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, required=True)
    description = forms.CharField(label='Description', max_length=100, required=False)


################################################
############### Delete a Category ##############
################################################
@view_function
@permission_required('catalog.delete_category', login_url='/homepage/index/')
def delete(request):
    '''Deletes a category'''
    try:
        c = cmod.Category.objects.get(id=request.urlparams[0])
    except cmod.category.DoesNotExist:
        return Http404()

    # Delete the event
    c.delete()

    # Redirect
    return HttpResponseRedirect('/manager/categories/')
