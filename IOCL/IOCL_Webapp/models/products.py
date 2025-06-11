from django.db import models

class Product(models.Model):
    description =  models.CharField(max_length=50,default='', blank='True', null='True')
    text = models.TextField(max_length=200, default='')
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    @staticmethod
    def get_all_products():
        return Product.objects.all()