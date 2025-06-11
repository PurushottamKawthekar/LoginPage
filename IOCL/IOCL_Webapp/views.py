from dbm.sqlite3 import GET_SIZE
from itertools import product
from symtable import Class

import objects
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render

from .models.products import Product
from .models.user import User
from django.contrib import messages
from .forms import UserForm, ProductForm
from django.shortcuts import get_object_or_404
from .models import User
from django.views import View
from IOCL_Webapp.models import User

# Create your views here.
#=====================Homepage============================================#

def home(request):
    return render(request, 'Home.html')

#=======================Signup=======================================#


@csrf_protect
def signup(request):
    global error_message
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        postData = request.POST
        name = postData.get('name').strip()
        phone = postData.get('phone').strip()
        aadhaar = postData.get('aadhaar').strip()
        #print(name,phone)
        user = User(name=name, phone=phone, aadhaar=aadhaar)
        error_message = None

        if not name:
            error_message = "Name is required !!!"
        elif any(char.isdigit() for char in name):
            error_message = "Name cannot contain numbers !!!"

        elif not phone:
            error_message = "Mobile Number is required !!!"
        elif not phone.isdigit():
            error_message = "Mobile Number must contain digits !!!"
        elif len(phone) < 10:
            error_message = "Mobile Number should be of 10 digits !!!"

        elif not aadhaar:
            error_message = "Aadhaar Number is required !!!"
        elif not aadhaar.isdigit():
            error_message = "Aadhaar Number must contain only digits!!!"
        elif len(aadhaar) < 12:
            error_message = "Aadhaar Number should be of 12 digits !!!"

        if not error_message:
            messages.success(request, 'Congratulations !!! You have been registered successfully...')
            user.save()
            return redirect('login')
        else:
            return render(request, 'signup.html', {'error':error_message, 'value':{'name': name,'phone':phone,'aadhaar':aadhaar}})

#========================================Login===============================================#

class Login(View):
    def get(self, request):
        return render(request, 'login.html')
    def post(self, request):
        phone = request.POST.get('phone')
        error_message = None
        value = {
            'phone': phone
        }

        users = User.objects.filter(phone=phone)
        if users.exists():
            request.session['phone'] = phone
            return redirect('user_list')
        else:
            error_message = "Mobile Number is Invalid !!!"
            data = {
                'error': error_message,
                'value': value
            }
            return render(request, "login.html", data)
#===============================================User_List====================================#

def user_list(request):
    products = Product.get_all_products()
    return render(request, 'user_list.html', {'products': products })



#====================================User_Create================================================#

def user_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            return redirect('user_list')
    else:
        form = ProductForm()
    return render(request, 'user_form.html', {'form': form})

#==========================================User_Edit====================================#

def user_edit(request, user_id):
    product = get_object_or_404(Product, pk=user_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = ProductForm(instance=product)

    return render(request, 'user_form.html', {'form': form})

#===========================================User_Delete===================================#


def product_delete(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        product.delete()
        return redirect('user_list')

    return render(request, 'user_confirm_delete.html', {'product': product})