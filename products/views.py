import datetime

from django.shortcuts import render

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
        'list_group_products': [
            {'name': 'Новинки',
             'link': '#'},
            {'name': 'Одежда',
             'link': '#'},
            {'name': 'Обувь',
             'link': '#'},
            {'name': 'Аксессуары',
             'link': '#'},
            {'name': 'Подарки',
             'link': '#'}
        ],
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals',
             'price': '6 090,00 руб.',
             'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'
             },

            {'name': 'Синяя куртка The North Face',
             'price': '23 725,00 руб.',
             'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.'
             },
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
             'price': '3 390,00 руб.',
             'description': 'Материал с плюшевой текстурой. Удобный и мягкий.'
             },
            {'name': 'Черный рюкзак Nike Heritage',
             'price': '2 340,00 руб.',
             'description': 'Плотная ткань. Легкий материал.'
             },
            {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
             'price': '13 590,00 руб.',
             'description': 'Гладкий кожаный верх. Натуральный материал.'
             },
            {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN',
             'price': '2 890,00 руб.',
             'description': 'Легкая эластичная ткань сирсакер Фактурная ткань.'
             }
        ],
        'button_add': 'Отправить в корзину',
        'button_delete': 'Удалить из корзины',
        'nav_bar_auth': 'Войти',
        'nav_bar_catalog': 'Каталог'
    }
    return render(request, 'products/products.html', context_produsts)

