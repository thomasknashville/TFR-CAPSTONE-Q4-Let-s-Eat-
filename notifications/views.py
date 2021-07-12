from django.shortcuts import render, reverse, HttpResponseRedirect
from users.models import TFRUser

# Create your views here.


# match user A favs w user B favs = match list
# match list * random = result



'''
class Note(models.Model):
    user = models.ForeignKey(
        TwitterUser, on_delete=models.CASCADE
    )
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tweet.content
'''
