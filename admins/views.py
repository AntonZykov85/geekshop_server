from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.contrib import messages
from users.models import User
from admins.forms import UserAdminRegistrationForm, UserAdminProfileForm

@user_passes_test(lambda u: u.is_staff)
def index(request):
    return render(request, 'admins/index.html')

@user_passes_test(lambda u: u.is_staff)
def admin_users(request):
     context = {
         'title': 'Админ-панель - Пользователи',
         'users': User.objects.all()}
     return render(request, 'admins/users_read.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_users_create(request):
     if request.method == 'POST':
         form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
         if form.is_valid():
             form.save()
             return HttpResponseRedirect(reverse('admins:admin_users'))
     else:
         form = UserAdminRegistrationForm()
     context = {'title': 'Админ-панель - Создание пользователя', 'form': form}
     return render(request, 'admins/user_create.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_users_update(request, id):
     selected_user = User.objects.get(id=id)
     if request.method == 'POST':
         form = UserAdminProfileForm(instance=selected_user, files=request.FILES, data=request.POST)
         if form.is_valid():
             form.save()
             return HttpResponseRedirect(reverse('admins:admin_users'))
     else:
         form = UserAdminProfileForm(instance=selected_user)
     context = {
         'title': 'Админ-панель - Редактирование пользовтаеля',
         'form': form,
         'selected_user': selected_user,
     }
     return render(request, 'admins/users_update_delete.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_users_delete(request, id):
     user = User.objects.get(id=id)
     user.safe_delete()
     return HttpResponseRedirect(reverse('admins:admin_users'))