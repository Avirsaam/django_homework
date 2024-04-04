from django.core.management.base import BaseCommand
from homeworkapp.models import Product, Client, Order
from random import choice, randint

class Command(BaseCommand):
    help = "Очистить таблицы клиенты, товары, заказы"
    
    
    def handle(self, *args, **kwargs):
        orders = Order.objects.all()        
        for order in orders:
            order.delete()
        
        products = Product.objects.all()
        for product in products:
            product.delete()
            
        clients = Client.objects.all()
        for client in clients:
            client.delete()
        
        
        
