from django.shortcuts import render, reverse, HttpResponseRedirect
from users.models import TFRUser

# Create your views here.


# match user A favs w user B favs = match list
# match list * random = result
def get_fav(request, id):
    my_favs = TFRUser.objects.all(id=id)
    user_favs = request.user.filter(favorites=id)
    match_list = []
    for i in my_favs:
        for j in user_favs:
            if i == j:
                match_list.add(i)
    return render(request, 'index.html', {'match_list': match_list})


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
