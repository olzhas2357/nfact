from django.shortcuts import render
from django.http import HttpResponse
from .models import Shop
def home(request):
    shop = Shop.objects.all()
    return render(request, 'home.html', {'shop': shop})