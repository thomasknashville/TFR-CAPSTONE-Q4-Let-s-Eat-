from restaurants.models import Restaurant
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from users.models import TFRUser

# Create your views here.


@login_required
def rest_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'index.html', {'restaurants': restaurants})


def restaurant_detail(request, restaurant_id: int):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    return render(request, 'restaurant_detail.html', {'restaurant': restaurant})


def add_to_favs(request, restaurant_id: int):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    user = TFRUser.objects.get(id=request.user.id)
    user.favorites.add(restaurant)
    user.save()
    return HttpResponseRedirect(reverse('restaurant_detail.html'))
