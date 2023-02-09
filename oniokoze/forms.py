from django import forms
import os
import logging
from django.urls import reverse_lazy
from django.views import generic
from .models import *
from django.forms.models import inlineformset_factory
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
import json
from accounts.models import CustomUser

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
        fields = (
            'name',
            'size'
        )


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
        fields = (
            'method',
            'title',
            'shopphoto',
            'shopURL',
            'titlephoto'
        )
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields.values():
                field.widget.attrs['class'] = 'form-control'
class SpotCreateForm(forms.ModelForm):
    class Meta:
        model=Spot
        fields=('capital', 'city', 'address','place', 'location','spotURL','free','beginner')
        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.value():
                field.widget.attrs['class']='form-control'

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'order',
            'procedure',
            'material',
            'amount',
            'unit'
        )


        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields.values():
                field.widget.attrs['class'] = 'form-control'

        def form_valid(self, form):
            order = form.save(commit=False)
            order.save()
            return super().form_vaild(form)

        def add_prefix(self, field_name):
            field_name = FIELD_NAME_MAPPING.get(field_name, field_name)
            return super(OrderCreateForm, self).add_prefix(field_name)


class MypageCreateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = (
            'username',
            'photo',
            'email',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class FishCreateForm(forms.ModelForm):
    class Meta:
        model = Fish
        fields = (

            'fish',
        )


        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields.values():
                field.widget.attrs['class'] = 'form-control'

        def form_valid(self, form):
            fish = form.save(commit=False)
            fish.save()
            return super().form_vaild(form)

        def add_prefix(self, field_name):
            field_name = FIELD_NAME_MAPPING.get(field_name, field_name)
            return super(FishCreateForm, self).add_prefix(field_name)