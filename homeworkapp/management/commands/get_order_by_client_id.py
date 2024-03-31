from django.core.management.base import BaseCommand
from homeworkapp.models import Client, Product, Order


class Command(BaseCommand):
    help = "Получить заказ по ID клиента"
    
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='ID клиента')
        
    
    def handle(self, *args, **kwargs):
        pk = kwargs['pk']                                        
        result = Order.objects.filter(client=pk).all()
        self.stdout.write(f'{result}')
        
