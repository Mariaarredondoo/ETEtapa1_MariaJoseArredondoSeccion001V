from django import forms
from django.db.models.base import Model
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Registro

class RegistroForm(forms.ModelForm):
    class Meta:
        model= Registro
        fields=['numIdentificacion',
        'fotografia',
        'nomCompleto',
        'telefono',
        'direccion',
        'mail',
        'pais',
        'contraseña',
        'monedaPago'
        ]
        labels={'numIdentificacion':'Número de indentificación:',
        'fotografia':'Fotografía:',
        'nomCompleto':'Nombre Completo: ',
        'telefono':'Teléfono (+569):',
        'direccion':'Dirección:',
        'mail':'Email:',
        'pais':'País:',
        'contraseña':'Contraseña:',
        'monedaPago':'Moneda de pago:'

        }
        widgets={
            'numIdentificacion':forms.TextInput(
                attrs={
                    'id': 'numIden',
                    'name': 'numIden',
                    'placeholder': '1111',
                    'autofocus': True,
                    'required':True,
                }
            ),
            'fotografia':forms.ClearableFileInput(
                attrs={
                    'id': 'foto',
                    'name': 'foto',
                    'required':True,
                }
            ),
            'nomCompleto':forms.TextInput(
                attrs={
                    'id': 'nom',
                    'name': 'nom',
                    'placeholder': 'Ingrese su nombre completo',
                    'autofocus': True,
                    'required':True,
                }
            ),
            'telefono':forms.TextInput(
                attrs={
                    'id': 'phono',
                    'name': 'phono',
                    'placeholder': '1111 1111',
                    'autofocus': True,
                    'required':True,
                }
            ),
            'direccion':forms.TextInput(
                attrs={
                    'id': 'dire',
                    'name': 'dire',
                    'placeholder': 'Ingrese su dirección',
                    'autofocus': True,
                    'required':True,
                }
            ),
            'mail':forms.EmailInput(
                attrs={
                    'id': 'mail',
                    'name': 'mail',
                    'placeholder': 'Ingrese su email',
                    'autofocus': True,
                    'required':True,
                }
            ),
            'pais':forms.TextInput(
                attrs={
                    'id': 'pais',
                    'name': 'pais',
                    'placeholder': 'Ingrese su país',
                    'autofocus': True,
                    'required':True,
                }
            ),

           'contraseña':forms.PasswordInput(
                attrs={
                    'id': 'pass',
                    'name': 'pass',
                    'placeholder': 'Ingrese su contraseña',
                    'autofocus': True,
                    'required':True,
                }
            ), 
            'monedaPago':forms.TextInput(
                attrs={
                    'id': 'mon',
                    'name': 'mon',
                    'placeholder': 'Ingrese tipo de moneda de pago',
                    'autofocus': True,
                    'required':True,
                }
            ),
        }
