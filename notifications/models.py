from restaurants.models import Restaurant
from django.db import models
from users.models import TFRUser
from django.utils import timezone
# Create your models here.


class Notification(models.Model):
    read = models.BooleanField(default=False)
    sender = models.CharField(max_length=200, null=True)
    recipient = models.ForeignKey(
        TFRUser, on_delete=models.CASCADE)
    rest_match = models.ForeignKey(Restaurant, on_delete=models.CASCADE, blank=True)
    created_at =models.DateTimeField(default=timezone.now)


Notification.objects.order_by('created_at')

    # def __str__(self):
    #     return self.match


# class Note(models.Model):
#     user = models.ForeignKey(
#         TwitterUser, on_delete=models.CASCADE
#     )
#     tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.tweet.content
