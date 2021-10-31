from django.contrib import admin
from products.models import ProductCategory, Products

admin.site.register(ProductCategory)

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'image', ('price', 'quantity'), 'category', 'description')
    readonly_fields = ('description',)
