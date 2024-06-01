# from django.urls import path
# from . import views
# urlpatterns = [
#     path('home', views.home)
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:pk>', views.details, name='details'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_detail, name='cart_detail'),
]
