from django.contrib import admin
from .user.Usermodel import Profile
from .models import Product, Category, Order, OrderItem

# Register your models here.
admin.site.register(Profile)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem)
