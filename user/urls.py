from django.urls import path
from . import views
urlpatterns = [
    path('signup', views.SignUpPage, name='signup'),
    path('login', views.LoginPage, name='login'),
    path('profile', views.ProfilePage, name='profile'),
    path('logout', views.LogOutPage, name="logout"),
    
]