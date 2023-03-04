from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserModel (models.Model):   
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    bio = models.TextField(blank=True, null=True)
    cv = models.FileField(blank=True, null=True, upload_to="mycv")
    profile = models.ImageField(blank=True, null=True , upload_to='profile' )
    project_1 = models.TextField(blank=True, null=True)
    project_2 = models.TextField(blank=True, null=True)
    

class Contacts(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
