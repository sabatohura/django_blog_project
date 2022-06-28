from dataclasses import field, fields
from pyexpat import model
from statistics import mode
from django import forms

from django.contrib.auth import get_user_model
from blogapp.models import Blog, User

User = get_user_model()

class UserRegistration(forms.ModelForm):
    class Meta:
        model=User
        fields = '__all__'

class BlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields='__all__'