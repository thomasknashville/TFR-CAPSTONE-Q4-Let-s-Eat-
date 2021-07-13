from django.shortcuts import render, reverse, HttpResponseRedirect
from users.models import TFRUser
from notifications.models import Notification

# Create your views here.


# match user A favs w user B favs = match list
# match list * random = result


# app_choice goes to a folder

# when a user signs in, loop through the app_choice objects 
# and find any with that user as user their_favs 
# grab their profile page and append the app_choice item to their inbox

def note(request, user_id):
    notes = Notification.objects.all()
    return render(request, 'other_user.html', {'notes': notes})





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
