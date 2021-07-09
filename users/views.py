from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from users.forms import SignupForm, LoginForm, ImageForm
from users.models import TFRUser
from django.contrib.auth import authenticate, logout, login

'''home page is user_profile'''


def profile():
    '''profile info
    favs
    friends 
    link to restaurants page to choose favs
    notifications'''


def favorites():
    ...


def remove_fav():
    ...


@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'form.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'form.html', {'form': form})
