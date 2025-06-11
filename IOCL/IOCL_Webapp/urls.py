from django.contrib import admin
from django.urls import path
from .views import home, signup
from IOCL_Webapp import views
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('signup', views.signup , name='signup'),
    path('login', views.Login.as_view() , name='login'),
    path('users', views.user_list , name='user_list'),
    path('create', views.user_create , name='user_create'),
    path('<int:user_id>/edit/', views.user_edit , name='user_edit'),
    path('<int:product_id>/delete/', views.product_delete , name='user_delete'),

]
