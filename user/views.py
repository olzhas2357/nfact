from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError

@login_required(login_url='login')
def ProfilePage(request):
    return render (request, 'profile.html')     
    
def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else: 
            return HttpResponse( "Username or Password is incorrect")
    return render (request, 'login.html')

def SignUpPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return render(request, 'registration_error.html', {'error_message': 'Your password and confrom password are not Same :('})
        else:
            try:
                my_user = User.objects.create_user(username=uname, email=email, password=pass1)
                my_user.save()
                return redirect('login')
            except IntegrityError:
                if User.objects.filter(username=uname).exists() and User.objects.filter(email=email).exists():
                    return render(request, 'registration_error.html', {'error_message': 'A user with this username or email already exists.'})
                return redirect('login')
            
    return render (request, 'signup.html')

def LogOutPage(request):
    logout(request)
    return redirect('login')