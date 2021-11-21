from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate

from users.forms import UserLoginForm


def create_user(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'users/create_users.html', context=context)


def profile_view(request):
    return render(request, 'users/user_profile.html')


def user_login(request):
    form = UserLoginForm()
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_password = form.cleaned_data['password']
            user = authenticate(request, username=user_name, password=user_password)
            if user:
                login(request, user)

            return redirect('user-profile')

    context = {'form': form}
    return render(request, 'users/user_profile.html', context=context)