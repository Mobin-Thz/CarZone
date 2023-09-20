from django.db import models
   
# Create your models here.

class User(models.Model):
    firstname = models.CharField(max_length=200,)
    lastname = models.CharField(max_length=200,)
    username = models.CharField(max_length=200,)
    email = models.EmailField()

