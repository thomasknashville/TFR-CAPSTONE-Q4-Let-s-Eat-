from notifications.models import Notification
from django.shortcuts import render
from users.models import TFRUser
import random
# Create your views here.
def get_fav(request, user_id: int):
    other_user = TFRUser.objects.get(id=user_id)
    my_favs = TFRUser.objects.get(id=request.user.id).favorites.all()
    their_favs = TFRUser.objects.get(id=user_id).favorites.all()
    match_list = []
    for i in my_favs:
        for j in their_favs:
            if i == j:
                match_list.insert(0, i)
    if match_list == []:
        app_choice = "You have no restaurants in common! Pick another favorite and try again!"
    else:
        app_choice = random.choice(match_list)
        Notification.objects.create(
            recipient = other_user,
            rest_match = app_choice,
            sender = request.user,
        )
    return render(request, 'match.html', {'app_choice': app_choice})


    

