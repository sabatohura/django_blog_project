import imp
from operator import index
from unicodedata import name
from . import views
from django.urls import path,URLPattern

urlpatterns = [
    path("",views.blog,name="blog_index")
]