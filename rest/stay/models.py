from django.db import models
from django import forms

class UserProfile(models.Model) :
    name = models.CharField(max_length=30,default='Anshul')
    email = models.EmailField(max_length=120)
    phone_no = models.CharField(max_length=20)
    message = models.TextField(max_length=200)




class UserForm(forms.ModelForm):
    class Meta:
        model= UserProfile
        fields= ['name','email','phone_no','message']
