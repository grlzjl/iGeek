from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('query', views.query),
    path('write', views.write),
    path('login', views.login),
    path('register1', views.register1),
    path('person', views.person),
    path('income', views.income),
]