from django.db import models

# Create your models here.

class Team (models.Model):
    first_name = models.CharField(max_length=100,)
    last_name = models.CharField(max_length=100,)
    image = models.ImageField(upload_to='photos/%Y/%M/%D/',null=True,blank= True,)
    designation = models.CharField(max_length=100,)
    instagram_link = models.URLField(max_length=100,null=True,blank= True,)
    facebook_link = models.URLField(max_length=100,null=True,blank= True,)
    created = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.first_name
