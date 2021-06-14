from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order


# This will change the header of table of "Products" section
class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


# This will change the header of table of "Categorys" section
class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


# This will change the header of table of "Customers" section
class AdminCustomer(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone']


# This will change the header of table of "Customers" section
class AdminOrder(admin.ModelAdmin):
    list_display = ['product', 'quantity', 'customer', 'phone', 'date', 'status']


# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer, AdminCustomer)
admin.site.register(Order, AdminOrder)