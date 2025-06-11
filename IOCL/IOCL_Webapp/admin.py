from django.contrib import admin
from .models.user import User
from .models.products import Product
# Register your models here.

class AdminUser(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'aadhaar']

class AdminProduct(admin.ModelAdmin):
    list_display = ['description', 'text', 'photo', 'created_at', 'updated_at']



admin.site.register(User, AdminUser)
admin.site.register(Product, AdminProduct)
