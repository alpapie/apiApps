from django import forms
from django.db import models
from django.forms import fields
from django.contrib.auth.models import User
from .models import contact

class ContactForm(forms.ModelForm):
    class Meta:
        model=contact       
        fields=['nom','prenom','email','telephone','age','location','icon']
class Conection(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password']