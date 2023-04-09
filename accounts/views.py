from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User
# Create your views here.


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            print('yeah')
            login(request, user)
        else:
            print('fail')
    return render(request, 'erp/product_list.html')


@login_required
def signout(request):
    logout(request)
    return redirect('user:signin')


def signup(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']

        user = User.objects.create_user(username, email, password)
        user.first_name = firstname
        user.last_name = lastname
        user.save()
        return redirect('user:signin')
    else:
        return render(request, 'accounts/signup.html')
