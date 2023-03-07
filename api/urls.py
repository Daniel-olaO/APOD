from django.urls import path
from .views import index, register, login, getUsers, logOut, toggleSubscriptions

urlpatterns = [
    path('', index),
    path('register', register),
    path('login', login),
    path('users', getUsers),
    path('logout', logOut),
    path('toggle-subscription/<int:id>/', toggleSubscriptions)
]