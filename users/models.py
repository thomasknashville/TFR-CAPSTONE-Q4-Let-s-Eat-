from restaurants.models import Restaurant
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class TFRUser(AbstractUser):
    email = models.EmailField(null=True, blank=True)
    bio = models.TextField(max_length=250, blank=True)
    favorites = models.ManyToManyField(
        Restaurant, symmetrical=False, related_name="my_favs", default=0)

    def __str__(self):
        return self.username

class Image(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title

