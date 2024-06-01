# from django.urls import path
# from . import views
# urlpatterns = [
#     path('home', views.home)
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('product/<int:pk>', views.details, name='details'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('cart_detail/', views.cart_detail_view, name='cart_detail'),
    path('search/', views.search, name='search')
]
