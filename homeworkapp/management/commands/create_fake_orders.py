from django.core.management.base import BaseCommand
from homeworkapp.models import Product, Client, Order
from random import choice, randint
from datetime import datetime, timedelta
class Command(BaseCommand):
    help = "Заполнить базу заказами"
    
    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Количество заказов')
        
    
    def handle(self, *args, **kwargs):
        count = kwargs['count']
        
        clients = Client.objects.all()
                        
        for _ in range(count+1):            
            order = Order(client=choice(clients),
                          created=datetime.now() - timedelta(days=randint(10,60), 
                                                             hours=randint(1,24),
                                                             minutes=randint(0, 60),
                                                             seconds=randint(0,60))
                          )            
            order.save()
        
        orders = Order.objects.all()
        products = Product.objects.all()
            
        for order in orders:
            for _ in range(randint(1, 6)):
                order.products.add(choice(products))
            
            order.save()
            self.stdout.write(f'{order}')
        
