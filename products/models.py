from django.db import models

# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length=120, unique=True)
    description = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=256, unique=True)
    image = models.ImageField(upload_to='products_images', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} | {self.category.name}'
