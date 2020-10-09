
from django import forms
from django.db import models


class UserProfile2(models.Model) :
    name = models.CharField(max_length=30,default='Anshul')
    username = models.CharField(max_length=120,unique=True)
    password = models.CharField(max_length=200)
    email = models.EmailField(max_length=20)


class UserForm2(forms.ModelForm):
    class Meta:
        model= UserProfile2
        fields= ['name','username','password','email']
