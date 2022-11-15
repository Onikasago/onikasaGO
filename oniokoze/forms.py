from django import forms
import os
from .models import Catch,Fishname


class CatchCreateForm(forms.ModelForm):


    class Meta():

        model = Catch
        fields = (
            'capital', 'city', 'address', 'location', 'free'
        )

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields.values():
                field.widget.attrs['class'] = 'form-control'



class FishnameCreateForm(forms.ModelForm):


    class Meta():

        model = Fishname
        fields = (
            'name', 'size'
        )
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields.values():
                field.widget.attrs['class'] = 'form-control'

