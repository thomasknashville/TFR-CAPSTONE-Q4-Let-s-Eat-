from django.db import models

# Create your models here.


class Restaurant(models.Model):
    name = models.TextField(max_length=200)
    location = models.TextField(max_length=200)
    pic_icon = models.ImageField(
        upload_to=None, height_field=None, width_field=None, max_length=None)
    sig_dish = models.TextField(max_length=200)
    num_favs = models.IntegerField(default=0)

    def __str__(self):
        return self.name
