from django import forms
from .models import Tarea

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo','descripcion','completo']
        # widgets = {
        #     'titulo': forms.TextInput(attrs={'class': 'form-control'}),
        #     'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
        #     'completo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        # }
