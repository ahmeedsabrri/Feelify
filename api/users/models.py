from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    avatar = models.URLField()
    
    def __str__(self):
        return self.username