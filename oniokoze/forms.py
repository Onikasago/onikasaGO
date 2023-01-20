from django import forms
import os
import logging
from django.urls import reverse_lazy
from django.views import generic
from .models import *
from django.forms.models import inlineformset_factory
# from django_superform import ModelFormField, SuperModelForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404

FIELD_NAME_MAPPING = {
    'titleList': 'titleList_0',
    'bodyList': 'bodyList_0',
    'noList': 'noList_0',
    'idList': 'idList_0',
}
class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        catch = get_object_or_404(Fishname, pk=self.kwargs['pk'])
        return self.request.user == list.user


class CatchCreateForm(forms.ModelForm):
    class Meta:
        model = Catch
        fields = (
            'nametitle',
            'photo1',
            'capital',
            'city',
            'address',
            'place',
            'location',
            'free',
        )

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields.values():
                field.widget.attrs['class'] = 'form-control'



CatchFormset = forms.inlineformset_factory(
    Catch,Fishname, fields='__all__',
    extra=2,max_num=5, can_delete=False
)

class FishnameCreateForm(forms.ModelForm):
    class Meta:
        model = Fishname
        fields = '__all__'


        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields.values():
                field.widget.attrs['class'] = 'form-control'

        def form_valid(self, form):
            fishname = form.save(commit=False)
            fishname.save()
            return super().form_vaild(form)

        def add_prefix(self, field_name):
            field_name = FIELD_NAME_MAPPING.get(field_name, field_name)
            return super(FishnameCreateForm, self).add_prefix(field_name)

class RecipeCreateForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields =  '__all__'