from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from Control import forms, views



urlpatterns = [
   path('', views.direcionar),
   path('logar/', views.logar, name='logar'),
   path('#/', views.autenticar, name='autenticar'),
   path('#/consultar/', views.consultar, name='consultar'),
   path('#/consultar/json', views.jsonResponse, name='jsonResponse'),
   path('#/consultar/deslogar', views.deslogar, name='deslogar'),
]