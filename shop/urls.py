from django.urls import path
from . import views
urlpatterns = [
    path('home', views.home)
]
from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home),
    path('home/<int:pk>', views.details, name='details'),
]
