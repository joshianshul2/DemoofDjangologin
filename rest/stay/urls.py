from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('temp', views.index2,name='index2'),



]
