"""
URL configuration for Quantum project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from Cure import views
from django.urls import path
from . import views
urlpatterns = [
    path('', views.hospital, name='hospital'),
    path('home/', views.dental_home, name='dental_home'),
    path('home2', views.dental_home, name='dental_home'),
    path('about/', views.dental_about, name='dental_about'),
    path('services/', views.dental_services, name='dental_services'),
    path('doctors/', views.dental_doctors, name='dental_doctors'),
    path('blog/', views.dental_blog, name='dental_blog'),
    path('index', views.pharmacy_index, name='pharmacy_index'),
    path('pharmacy_about', views.pharmacy_about, name='pharmacy_about'),
    path('pharmacy_cart', views.pharmacy_cart, name='pharmacy_cart'),
    path('pharmacy_checkout', views.pharmacy_checkout, name='pharmacy_checkout'),
    path('pharmacy_contact', views.pharmacy_contact, name='pharmacy_contact'),
    path('pharmacy_shop', views.pharmacy_shop, name='pharmacy_shop'),
    path('pharmacy_shopsingle', views.pharmacy_shopsingle, name='pharmacy_shopsingle'),
    path('pharmacy_thankyou', views.pharmacy_thankyou, name='pharmacy_thankyou'),
    path('book-appointment/', views.book_appointment, name='book_appointment'),
    path('apply_internship/', views.apply_internship, name='apply_internship'),
    path('index1', views.index_view, name='index'),
    path('blog1/', views.blog1, name='blog1'),
    path('blog2/', views.blog2, name='blog2'),
    path('blog3/', views.blog3, name='blog3'),
    path('apply/', views.apply_internship, name='apply_internship'),
    # path('signup/', views.signup_view, name='signup'),
    # path('login/', views.login_view, name='login'),
    # path('logout/', views.logout_view, name='logout'),
    path('quantumcare/', views.quantumcare, name='quantumcare'),
    path('lab_about', views.lab_about, name='lab_about'),
    path('lab_doctors', views.lab_doctors, name='lab_doctors'),
    path('lab_home', views.lab_home, name='lab_home'),
    path('lab_departments', views.lab_departments, name='lab_departments'),
    path('lab_contact', views.lab_contact, name='lab_contact'),
    path('depart_home/', views.depart_home, name='depart_home'),
    path('depart_about', views.depart_about, name='depart_about'),
    path('depart_doctors', views.depart_doctors, name='depart_doctors'),
    path('depart_news', views.depart_news, name='depart_news'),
    path('depart_action', views.depart_action, name='depart_action'),
    path('depart_contact', views.depart_contact, name='depart_contact'),
]
