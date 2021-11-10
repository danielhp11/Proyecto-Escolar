from django import forms
import datetime

from django.forms import fields

class FormCitaR(forms.Form):

    nombre = forms.CharField( label="Nombre", required= True )

    opciones_corte =[
        ('corto','Corto (Caballero)'),
        ('mediano','Mediano (A la altura de los hombros)'),
        ('largo', 'Largo (Más abajo de los hombros)')
        ]
    
    cabello = forms.TypedChoiceField(
        label= "Largo de cabello",
        choices= opciones_corte
    )

#CLASE PARA UN FORMULARIO PERSONALIZADO CON DJANGO

from django.core import validators

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        #Campos a pedir usuario, email == telefono, 
        fields = ['username','email','password1','password2']