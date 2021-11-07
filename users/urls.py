from django.urls import path

from users.views import login, profile, registration, logout
#ProfileUpdateView, RegistrationCreateView

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    ##path('registration/<int:pk>/', RegistrationCreateView.as_view(), name='registration'),
    path('logout/', logout, name='logout'),
   # path('profile/<int:pk>', ProfileUpdateView.as_view(), name='profile'),
    path('profile/', profile, name='profile'),
    path('registration/', registration, name='registration'),

]
