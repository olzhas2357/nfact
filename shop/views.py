from django.shortcuts import render
from django.http import Http404
from .models import Shop

def home(request):
    shop = Shop.objects.all()
    return render(request, 'home.html', {'shop': shop})

def details(request, pk):
    try:
        card = Shop.objects.get(pk=pk)
    except Shop.DoesNotExist:
        raise Http404('Shop does not exist')
    
    return render(request, 'details.html', {'card': card})
