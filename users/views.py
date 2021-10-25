from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.contrib import messages
from baskets.models import Basket
from django.contrib.auth.decorators import login_required



def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
        else:
                print(form.errors)
    else:
        form = UserLoginForm()
    context = {'title' : 'GeekShop - авторизация', 'form' : form}
    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Вы успешно зарегистрированы!")
            return HttpResponseRedirect(reverse('users:login'))
        else: print(form.errors)
    else:
        form = UserRegistrationForm()
    context = {'title': 'GeekShop - Регистрация', 'form': form}
    return render(request, 'users/registration.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files = request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Данные упешно изменены!")
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=request.user)
    context = {
            'title': 'GeekShop - Профиль',
            'form': form,
            'baskets': Basket.objects.all(),
            }
    return render(request, 'users/profile.html', context)