from django import forms

class OniokozeCreateForm(forms.ModelForm):
    class Meta:
        model = Catch
        fields = ('name1', 'name2', 'name3', 'name4', 'name5',
                  'photo1', 'photo2', 'photo3', 'photo4', 'photo5',
                  'size1', 'size2', 'size3', 'size4', 'size@:0.5',
                  'capital', 'city', 'address', 'location', 'free',
                  'created_at', 'updated_at', 'linecount')

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields.values():
                field.widget.attrs['class'] = 'form-control'





