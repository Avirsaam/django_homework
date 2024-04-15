from django.views import View
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.files.storage import FileSystemStorage

from .models import *
from .forms import ProductEditForm
from datetime import datetime, timedelta
import pytz


import logging

logger = logging.getLogger(__name__)



def index(request):
    context = {'text_content1': 'Et ipsum elit cillum proident cillum minim commodo elit. Ipsum pariatur sunt quis officia Lorem pariatur aute nisi sunt ad aute. Culpa fugiat voluptate id consequat occaecat officia culpa id do amet consequat. Ad consequat ad Lorem non sunt dolore nisi nostrud reprehenderit reprehenderit enim. In cupidatat excepteur nulla ut irure dolore reprehenderit incididunt tempor non. Ex adipisicing sit et et. Esse aliqua veniam cupidatat elit eu ullamco aute voluptate.',
            'picture_content1': 'https://dummyimage.com/600x400/000/b3b3b3.png',                        
    }
    logger.debug(f'index page assessed by {request.get_host()}')
    return render(request, "homeworkapp/index.html", context)
    

class AboutView(View):
    def get (self, request):
        address = {'building': '20',
               'street': 'Проспект Мира',
               'tel': '+7-987-654-32-11',
               'email': 'sales@myshop.rr'}
        context = {'address': address,
               'shop_photo': 'https://dummyimage.com/600x600/000/b3ff3b3.png'}
        return render(request, "homeworkapp/about.html", context)

class AllClientsView(View):
    def get(self, request):
        context = {
            "title": "All clients",
            "clients": Client.objects.all(),
            "total_orders": Order.objects.all().count()        
        }
        return render(request, 'homeworkapp/all_clients_template.html', context)

class ProductsByClient(View):
    def get(self, request, client_id, days):
        client = get_object_or_404(Client, pk=client_id)
        all_client_orders = Order.objects.order_by('-created').filter(client=client_id, created__gt=datetime.now()-timedelta(days=days)).all()
        products = {}
        for order in all_client_orders:
            for product in order.products.all():
                #cоздаем словарь с уникальными значениями товаров и их датами заказа
                last_product_date = products.setdefault(product.name, datetime.min.replace(tzinfo=pytz.UTC))
                products[product.name] = max(order.created, last_product_date)
                
        context = {
            "client":client,
            "products": products,
            "days": days
        }
        return render(request, "homeworkapp/all_products_by_client.html", context)

class ListOfCategories(View):
    def get(self, request):
        context = {'header': 'Категории товаров',
               'sub_header': ' ',
               'category_list': Category.objects.all(),
               }
        return render(request, 'homeworkapp/list_of_categories.html', context)
        
    
class ProductsByCategory(View):
    def get(self, request, category_id):
        
        header = 'Товары в категории:'
        category = Category.objects.filter(pk=category_id).first()
            
        context = {'header': header,
                   'category': category,
                   'products': Product.objects.filter(category=category).all()
                }
        return render(request, 'homeworkapp/products_by_category.html', context)
    
class ProductView(View):
    def get(self, request, product_id):        
        context = {
            "product" : Product.objects.filter(pk=product_id).first(),
        }
        return render (request, "homeworkapp/product_vew_template.html", context)
    
class ProductEditView(View):
    form_class = ProductEditForm
    template = 'homeworkapp/edit_product.html'
    context = {
            "title": "Редактирование карточки товара",            
            "button_caption" : "Добавить новый товар",
        }
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)        
        
        if form.is_valid():              
            product = Product.objects.filter(pk=int(form.cleaned_data['name_select'])).first()
            if product is None:
                logger.debug('Новый товар')
                product = Product()
            product.name = form.cleaned_data['name']
            product.description = form.cleaned_data['description']
            product.price = form.cleaned_data['price']
            product.stock = form.cleaned_data['stock']
            product.last_updated = datetime.now()                        
            image = form.cleaned_data['image']                        
            if image:
                product.image = image.name
                fs = FileSystemStorage()
                fs.save(image.name, image)
            else:
                #удаляем картинку если файл не выбран
                product.image = None
            product.save()                       
            
            return redirect('edit_product', product.id)
        else:
            return render(request, self.template, self.context)            
            
        

    def get(self, request, product_id=0):
        form_data = {
            'name_select': product_id,  
        }
        
        if product_id == 0:            
            self.context['button_caption'] = 'Добавить новый товар'
        else:
            product = Product.objects.get(pk=product_id)
            
            form_data['name'] = product.name
            form_data['description'] = product.description
            form_data['price'] = product.price
            form_data['stock'] = product.stock
            self.context['product_filename'] = product.image if product.image else "No image loaded"
            self.context['button_caption'] = 'Применить изменения'            
            self.context['product_image_url'] = f'/media/{product.image if product.image else "no_image.jpg"}'
            
                
                        
        self.context['form'] = self.form_class(initial=form_data)
        return render(request, self.template, self.context)