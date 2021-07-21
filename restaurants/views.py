from restaurants.models import Restaurant
from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from users.models import TFRUser
from notifications.models import Notification
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        restaurants = Restaurant.objects.all()
        template_name= "index.html"
        unread = Notification.objects.filter(read=False, recipient=request.user)
        count = len(unread)
        context= {"restaurants": restaurants, "count":count}
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
        context = {'restaurant': restaurant, 'fav_num': fav_num}
        return render(request, template_name, context)

class AddToFavsView(LoginRequiredMixin, View):
    def get(self, request, restaurant_id):
        restaurant = Restaurant.objects.get(id=restaurant_id)
        if restaurant not in request.user.favorites.all():
            request.user.favorites.add(restaurant)
            restaurant.num_favs += 1
            request.user.save()
            restaurant.save()
        return HttpResponseRedirect(reverse('homepage'))    
        

class RemoveFromFavs(LoginRequiredMixin, View):
    def get(self, request, restaurant_id):
        restaurant = Restaurant.objects.get(id=restaurant_id)
        if restaurant in request.user.favorites.all():
            request.user.favorites.remove(restaurant)
            restaurant.num_favs -= 1
            request.user.save()
            restaurant.save()
        return HttpResponseRedirect(reverse('homepage'))
