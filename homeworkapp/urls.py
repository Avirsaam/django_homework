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
from .views import *

urlpatterns = [    
    path('', ListOfCategories.as_view(), name='index'),
    path('about', AboutView.as_view(), name='about'),
    path('all_clients/', AllClientsView.as_view(), name='all_clients'),
    path('list_of_categories', ListOfCategories.as_view(), name='list_of_categories'),
    path('products_by_category/<int:category_id>', ProductsByCategory.as_view(), name='products_by_category'),
    path('product/<int:product_id>', ProductView.as_view(), name='product_view'),
    
    path('products_by_client/<int:client_id>/<int:days>/', ProductsByClient.as_view(), name='products_by_client'),    
    path('edit_product/', ProductEditView.as_view(), name='edit_product'),
    path('edit_product/<int:product_id>', ProductEditView.as_view(), name='edit_product')
]
