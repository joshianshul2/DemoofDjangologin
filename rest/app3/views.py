from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


def login(request) :
    if request.method == 'POST':
         username1 = request.POST['username']
         password1 = request.POST['password']
         from django.contrib import auth
         x = auth.authenticate(username=username1,password=password1)
         if x is None :
            return redirect('login')
         else :
            return redirect('/')

    return render(request,'login.html')