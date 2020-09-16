from django.shortcuts import render,redirect
# from django.http import HttpResponse
from django.views.generic import TemplateView

from .models import UserProfile,UserForm

def login(request) :
    return render(request,"login.html")

def index(request) :
    return render(request,"index.html")

# Create your views here.
def index2(request):
    form = UserForm
    data=UserProfile.objects.all()
    if request.method == 'POST' :
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

        # name1 = request.POST['name']
        # email1 =  request.POST['email']
        # no = request.POST['phone_no']
        # mess =request.POST['message']
        #
        # a = UserProfile(name=name1,email=email1,phone_no=no,message=mess)
        # a.save()

    return render(request,'index2.html',{'context': data})


class HomeView(TemplateView):
    template_name = 'home.html'