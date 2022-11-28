from django import forms
import os
import logging
from django.urls import reverse_lazy
from django.views import generic
from .models import Catch, Fishname
from django.forms.models import inlineformset_factory
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404


class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        catch = get_object_or_404(Fishname, pk=self.kwargs['pk'])
        return self.request.user == list.user


class CatchCreateForm(forms.ModelForm):
    class Meta:
        model = Catch
        fields = (
            'nametitle', 'photo1', 'capital', 'city', 'address', 'place', 'location', 'free'

        )

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields.values():
                field.widget.attrs['class'] = 'form-control'


class FishnameCreateForm(forms.ModelForm):
    class Meta:
        model = Fishname
        fields = (
            '__all__'
        )

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields.values():
                field.widget.attrs['class'] = 'form-control'

        def form_valid(self, form):
            catch = form.save(commit=False)
            catch.user = self.request.user
            catch.save()
            return super().form_vaild(form)
