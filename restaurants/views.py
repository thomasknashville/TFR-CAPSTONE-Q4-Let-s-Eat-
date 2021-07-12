from restaurants.models import Restaurant
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from users.models import TFRUser


# Create your views here.


def test(request):
    return render(request, 'border_test.html')


@login_required
def index(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'index.html', {'restaurants': restaurants})


def restaurant_detail(request, restaurant_id: int):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    users = TFRUser.objects.all()
    fav_num = 0
    for user in users:
        for restaurant_fav in user.favorites.all():
            if restaurant_fav == restaurant:    
                fav_num += 1
            # else error 500 YOU ALREADY FAVORITED THIS 
    return render(request, 'rest_detail.html', {'restaurant': restaurant, 'fav_num': fav_num})


def add_to_favs(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    request.user.favorites.add(restaurant)
    restaurant.num_favs += 1
    request.user.save()
    restaurant.save()
    return HttpResponseRedirect(reverse('rest_detail', args=(restaurant_id,)))

def remove_from_favs(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    request.user.favorites.remove(restaurant)
    restaurant.num_favs -= 1
    request.user.save()
    restaurant.save()
    return HttpResponseRedirect(reverse('rest_detail', args=(restaurant_id,)))
