from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

from users.forms import SignupForm, LoginForm, ProfileEditForm
from users.models import TFRUser
from notifications.models import Notification
from restaurants.models import Restaurant
from django.contrib.auth import authenticate, logout, login

'''home page is restaurant'''


def SignupView(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            TFRUser.objects.create_user(
                username=data['username'],
                email=data['email'],
                password=data['password']
            )
            return HttpResponseRedirect(reverse('homepage'))
        else:
            form = SignupForm()
            context={'form':form}
            return render(request, 'signup_login_form.html', context)
    form = SignupForm()
    return render(request, 'signup_login_form.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse('homepage')))
           
    form = LoginForm()
    return render(request, "signup_login_form.html", {'form': form})

@login_required
def profile(request, user_id: int):
    user = TFRUser.objects.get(id=user_id)
    users=TFRUser.objects.all()
    restaurants = Restaurant.objects.all()
    new_notes = Notification.objects.filter(read=False, recipient=request.user)
    print(new_notes)
    return render(request, 'profile.html', {'user':user, 'users':users, 'restaurants': restaurants, "new_notes": new_notes })


def profile_edit(request, user_id: int):
    profile = TFRUser.objects.get(id=user_id)

    if request.method == 'POST':
        print("print this mofo")
        form=ProfileEditForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            profile.bio = data['bio']
            profile.email = data['email']
            if data['picture']:
                profile.picture = data['picture']
            profile.save()
            return HttpResponseRedirect(reverse('profile', args=(user_id,)))

    form = ProfileEditForm(initial={
        'bio': profile.bio,
        'email': profile.email,
        'picture': profile.picture,
    })
    return render(request, 'form.html', {'form': form})


def demo_error(request):
    ...
    
@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

def remove_from_favs(request, restaurant_id, user_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    request.user.favorites.remove(restaurant)
    request.user.save()
    return HttpResponseRedirect(reverse('profile', args=(user_id, )))

def real_500_error(request):
    raise Exception("make response code 500")
