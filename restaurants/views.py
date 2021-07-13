from restaurants.models import Restaurant
from django.shortcuts import render, redirect, reverse
from users.models import TFRUser
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.


def test(request):
    return render(request, 'border_test.html')



class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        restaurants = Restaurant.objects.all()
        template_name= "index.html"
        context= {"restaurants": restaurants}
        return render(request, template_name, context)


class RestaurantDetailView(LoginRequiredMixin, View):
    def get(self, request, restaurant_id: int):
        template_name= "rest_detail.html"
        restaurant = Restaurant.objects.get(id=restaurant_id)
        users = TFRUser.objects.all()
        fav_num = 0
        for user in users:
            for restaurant_fav in user.favorites.all():
                if restaurant_fav == restaurant:    
                    fav_num += 1
                # else error 500 YOU ALREADY FAVORITED THIS 
        context = {'restaurant': restaurant, 'fav_num': fav_num}
        return render(request, template_name, context)

class AddToFavsView(LoginRequiredMixin, View):
    def get(self, request, restaurant_id):
        restaurant = Restaurant.objects.get(id=restaurant_id)
        request.user.favorites.add(restaurant)
        restaurant.num_favs += 1
        request.user.save()
        restaurant.save()
        return redirect(reverse('rest_detail', args=(restaurant_id,)))

class RemoveFromFavs(LoginRequiredMixin, View):
    def get(self, request, restaurant_id):
        restaurant = Restaurant.objects.get(id=restaurant_id)
        request.user.favorites.remove(restaurant)
        restaurant.num_favs -= 1
        request.user.save()
        restaurant.save()
        return redirect(reverse('rest_detail', args=(restaurant_id,)))
