from django.shortcuts import render
from users.models import TFRUser
# Create your views here.
def get_fav(request, user_id: int):
    # myself = TFRUser.objects.get(id=user_id)
    my_favs = TFRUser.objects.get(id=request.user.id).favorites.all()
    their_favs = TFRUser.objects.get(id=user_id).favorites.all()
    print(my_favs, their_favs)
    
    # my_favs = myself.favorites.filter(id=myself)
    # get_user = TFRUser.objects.get(id=request.user.id)
    # user_favs = get_user.favorites.filter(id=get_user)
    match_list = []
    # # print(my_favs, user_favs, match_list)
    for i in my_favs:
        for j in their_favs:
            if i == j:
                match_list.insert(0, i)
    return render(request, 'match.html', {'my_favs': my_favs, 'their_favs': their_favs, 'match_list': match_list})