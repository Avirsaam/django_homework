from django.views import View
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Client, Product, Order
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