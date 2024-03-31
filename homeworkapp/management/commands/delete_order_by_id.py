from django.core.management.base import BaseCommand
from homeworkapp.models import Client, Product, Order
from random import choice, randint

class Command(BaseCommand):
    help = "Добавить товары в заказ"
    
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Order ID')
        
    
    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        order = Order.objects.filter(pk=pk).first()
        if order is not None:            
            self.stdout.write(f'{order}')
            order.delete()
        else:
            self.stdout.write('Заказа с таким номером не существует')
        
