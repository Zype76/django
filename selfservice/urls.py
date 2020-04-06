from rest_framework.routers import DefaultRouter
from .views import search, index
from django.urls import path, include
from django.conf.urls import url, include

urlpatterns = [ 
  url(r'search/', search),
  url(r'index/', index)
]

