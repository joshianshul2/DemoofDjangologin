from django.db import models
from django import forms

class UserProfile2(models.Model) :
    name = models.CharField(max_length=30,default='Anshul')
    username = models.CharField(max_length=120)
    phone_no = models.CharField(max_length=20)
    password = models.CharField(max_length=200)




class UserForm2(forms.ModelForm):
    class Meta:
        model= UserProfile2
        fields= ['name','username','phone_no','password']
