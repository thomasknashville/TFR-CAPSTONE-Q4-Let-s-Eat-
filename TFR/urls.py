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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from users import views as user_views
from restaurants import views as rest_views
from users import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', rest_views.index, name='homepage'),
    path('login/', user_views.login_view, name='login'),
    path('logout/', user_views.logout_view, name='logout'),
    path('signup/', user_views.signup_view, name='signup'),
    path('restaurant/<int:restaurant_id>/', rest_views.restaurant_detail, name="rest_detail"),
    path('restaurant/<int:restaurant_id>/favorite/', rest_views.add_to_favs, name="favorite"),
    path('user/', user_views.users, name='user'),
    path('user/<int:user_id>/', user_views.profile, name='profile'),
    path('form/', views.image_upload_view),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)