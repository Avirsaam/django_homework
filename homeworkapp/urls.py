"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from .views import index, AboutView, AllClientsView, ProductsByClient

urlpatterns = [    
    path('', index, name='index'),
    path('about', AboutView.as_view(), name='about'),
    path('all_clients/', AllClientsView.as_view(), name='all_clients'),
    path('products_by_client/<int:client_id>/<int:days>/', ProductsByClient.as_view(), name='products_by_client'),
]
