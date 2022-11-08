from django import forms
import os
from .models import Catch

class CatchCreateForm(forms.ModelForm):
    class Meta:
        model = Catch
        fields = (
                  'capital', 'city', 'address', 'location', 'free'
                  )

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields.values():
                field.widget.attrs['class'] = 'form-control'





