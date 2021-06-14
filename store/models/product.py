from django.db import models
from .category import Category


class Product(models.Model):
    # create "name" field with max length of 50 characters
    name = models.CharField(max_length=50)
    # create "price" field with default value set to 0(zero)
    price = models.IntegerField(default=0)
    # create "category" field with ForeignKey parameter
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    # create "description" field with max length of 200chars and default value set to empty string ''
    description = models.CharField(max_length=200, default='', blank=True)
    # create "image" field with "upload_to" feature to save product images to "products" folder
    image = models.ImageField(upload_to='uploads/products/')

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_category_id(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()
