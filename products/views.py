import datetime

from django.shortcuts import render
from products.models import Products, ProductCategory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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

def products(request, category_id=None, page=1):
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
    if category_id:
        products = Products.objects.filter(category_id=category_id)
    else:
        products = Products.objects.all()
    paginator = Paginator(products, 3)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    context_produsts['products'] = products_paginator
    return render(request, 'products/products.html', context_produsts)
