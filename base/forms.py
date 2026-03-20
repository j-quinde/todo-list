from django import forms
from .models import Tarea
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'completo']
        # widgets = {
        #     'titulo': forms.TextInput(attrs={'class': 'form-control'}),
        #     'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
        #     'completo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        # }


class MyAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Usuario'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Contraseña'})


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Ingrese un nombre de usuario'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Ingrese una contraseña'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirme la contraseña'})
