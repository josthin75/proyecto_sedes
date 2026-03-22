# gestion_carnets/forms.py
from django import forms
from .models import Beneficiario

class BeneficiarioForm(forms.ModelForm):
    class Meta:
        model = Beneficiario
        # IMPORTANTE: Añade 'edad' y 'sexo' aquí
        fields = ['nombre', 'apellido', 'ci', 'direccion', 'telefono', 'rubro_empresa', 'edad', 'sexo']
        
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresar nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresar apellido'}),
            'ci': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresar ci'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresar direccion'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresar telefono'}),
            'rubro_empresa': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresar rubro empresa'}),
            # Nuevos campos con estilo
            'edad': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingresar edad'}),
            'sexo': forms.Select(attrs={'class': 'form-select'}),
        }