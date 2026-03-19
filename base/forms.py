from django import forms
from .models import Tarea
from django.contrib.auth.forms import AuthenticationForm

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo','descripcion','completo']
        # widgets = {
        #     'titulo': forms.TextInput(attrs={'class': 'form-control'}),
        #     'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
        #     'completo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        # }

class MyAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder':'Usuario'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Contraseña'})