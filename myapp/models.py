

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='customer_profile')
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=255)
    state = models.CharField(max_length=100)
    education = models.CharField(max_length=255)
    experience = models.TextField()
    country = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.user.username