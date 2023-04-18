from django.contrib.auth.models import AbstractUser
from django.db import models





#creating customUser, So i can add fields i want like name in below
class CustomUser(AbstractUser):
    name = models.CharField(null=True, blank= True, max_length=100)
