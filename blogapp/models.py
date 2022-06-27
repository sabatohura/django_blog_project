from pyexpat import model
from turtle import mode, title
from django.db import models
import uuid
from django.contrib.auth import get_user_model

User = get_user_model()

class Blog(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=100)
    content= models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)




