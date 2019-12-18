
from django.urls import path

from rest_framework_jwt.views import obtain_jwt_token

from . import views

urlpatterns = [
    path('login', obtain_jwt_token),
    path('logout', views.logout),
    path('register', views.register),
    path('password', views.password),
    path('profile', views.profile),
]