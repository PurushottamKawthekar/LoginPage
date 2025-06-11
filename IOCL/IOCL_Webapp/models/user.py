from django.db import models
from django.db.models.functions import NullIf


class User(models.Model):
    name = models.CharField(max_length=50, default="Anonymous")
    phone = models.CharField(max_length=13)
    aadhaar = models.CharField(max_length=12, null=True, blank=True)
    text = models.TextField(max_length=240)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.text[:10]}'

