from django.urls import path
from django import urls
from . import views

urlpatterns=[
  path('services/',views.services, name='services')

]