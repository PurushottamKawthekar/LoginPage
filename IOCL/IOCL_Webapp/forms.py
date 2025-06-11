from django import forms
from .models import  User
from .models import Product


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'phone', 'aadhaar']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['description', 'text', 'photo']