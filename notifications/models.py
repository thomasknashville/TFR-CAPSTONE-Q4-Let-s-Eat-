from restaurants.models import Restaurant
from django.db import models
from users.models import TFRUser
# Create your models here.


class Result(models.Model):
    user = models.ForeignKey(
        TFRUser, on_delete=models.CASCADE, related_name="notification")
    # match = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    ...

    def __str__(self):
        return self.match


# class Note(models.Model):
#     user = models.ForeignKey(
#         TwitterUser, on_delete=models.CASCADE
#     )
#     tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.tweet.content
