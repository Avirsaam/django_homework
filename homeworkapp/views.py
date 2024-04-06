from django.views import View
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.files.storage import FileSystemStorage

from .models import Client, Product, Order
from .forms import ProductEditForm
from datetime import datetime, timedelta
import pytz


import logging

logger = logging.getLogger(__name__)



def index(request):    
    context = {
        "title": "Главная страница",
        "header": "Заголовок главной страницы",
        "content": "Adipisicing culpa amet enim aute nostrud eiusmod velit aute."
    }
    logger.debug(f'index page assessed by {request.get_host()}')
    return render(request, "homeworkapp/simple_template.html", context)
class AboutView(View):
    def get (self, request):
        context = {
            "title": "About",
            "header": "Обо мне",
            "content": "Minim quis anim proident minim ex ea do et magna aliqua laboris."
        }
        logger.debug(f'"about" page assessed by {request.get_host()}')
        return render(request, "homeworkapp/simple_template.html", context)

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