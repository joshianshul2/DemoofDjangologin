from django.shortcuts import render,redirect
# from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from .models import UserProfile2,UserForm2

# Create your views here.
def signup(request) :
    form = UserForm2
    # data = UserProfile.objects.all()
    if request.method == 'POST':
       name= request.POST['name']
       username= request.POST['username']
       password = request.POST['password']
       email = request.POST['email']
       x = User.objects.create_user(first_name=name,username=username,password=password,email=email)
       x.save()
       return redirect('/')

    return render(request,'signup.html')