from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

from users.forms import SignupForm, LoginForm
from users.models import TFRUser
from django.contrib.auth import authenticate, logout, login

'''home page is user_profile'''


def signup_view(request):
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
            return render(request, 'signup_login_form.html', {'form': form})
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

def users(request):
    users=TFRUser.objects.all()
    return render(request, 'profile.html', {'users': users})

@login_required
def profile(request, user_id: int):
    user = TFRUser.objects.get(id=user_id)
    return render(request, 'profile.html', {'user':user})
    
@login_required
def favorites():
    ...


@login_required
def remove_fav():
    ...


@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
