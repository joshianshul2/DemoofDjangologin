from django.shortcuts import render,redirect
# from django.http import HttpResponse
from django.views.generic import TemplateView

from .models import UserProfile2,UserForm2

# Create your views here.
def signup(request) :
    form = UserForm2
    # data = UserProfile.objects.all()
    if request.method == 'POST':
        form = UserForm2(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'signup.html')