"""TFR URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from users import views as user_views
from restaurants import views as rest_views
from favorites import views as fav_views
from notifications import views as note_views
# import users
# from django.conf.urls import handler404, handler500

# handler404 = 'users.views.handler404'
# handler500 = 'users.views.handler500'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', rest_views.IndexView.as_view(), name='homepage'),
    path('login/', user_views.login_view, name='login'),
    path('logout/', user_views.logout_view, name='logout'),
    path('signup/', user_views.SignupView, name='signup'),
    path('restaurant/<int:restaurant_id>/', rest_views.RestaurantDetailView.as_view(), name="rest_detail"),
    path('restaurant/<int:restaurant_id>/favorite/', rest_views.AddToFavsView.as_view(), name="favorite"),
    path('restaurant/<int:restaurant_id>/unfavorite/', rest_views.RemoveFromFavs.as_view(), name="unfavorite"),
    path('restaurant/<int:restaurant_id>/<int:user_id>/removefav/', user_views.remove_from_favs, name="remove_from_favs"),
    path('user/<int:user_id>/', user_views.profile, name='profile'),
    path('user/<int:user_id>/edit/', user_views.profile_edit, name='profile_edit'),
    path('user/<int:user_id>/match/', fav_views.get_fav, name='match'),
    path('user/<int:user_id>/viewmatch/', note_views.note, name='view_match'),
    path('error/', user_views.real_500_error, name='500 error')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    