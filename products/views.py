import datetime

from django.shortcuts import render
from products.models import Products, ProductCategory

# Create your views here.

def index(request):

    context_index = {
        'date': datetime.datetime.now(),
        'title': 'GeekShop',
        'parag_1': 'Сегодня! Новые образы и лучшие бренды на GeekShop Store. \n Бесплатная доставка по всему миру! Аутлет: до -70% Собственный бренд. -20% новым покупателям',
        'h1_title': 'GeekShop',
        'button': 'Начать покупки',
        'nav_bar_auth': 'Войти',
        'nav_bar_catalog': 'Каталог'
    }
    return render(request, 'products/index.html', context_index)

def products(request):
    context_produsts = {
        'date': datetime.datetime.now(),
        'title': 'GeekShop - Каталог',
        'h1_products': 'GeekShop',
        'products': Products.objects.all(),
        'categories': ProductCategory.objects.all(),
        'button_add': 'Отправить в корзину',
        'button_delete': 'Удалить из корзины',
        'nav_bar_auth': 'Войти',
        'nav_bar_catalog': 'Каталог'
        }
    return render(request, 'products/products.html', context_produsts)
