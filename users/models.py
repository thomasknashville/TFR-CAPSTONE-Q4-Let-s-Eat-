from restaurants.models import Restaurant
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class TFRUser(AbstractUser):
    email = models.EmailField(null=True, blank=True)
    picture = models.ImageField(
        upload_to=None, height_field=None, width_field=None, max_length=100)
    bio = models.TextField(max_length=250)
    favorites = models.ManyToManyField(
        Restaurant, symmetrical=False, related_name="my_favs", default=0)

    def __str__(self):
        return self.username
