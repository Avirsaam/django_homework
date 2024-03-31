from django.core.management.base import BaseCommand
from homeworkapp.models import Client, Product, Order


class Command(BaseCommand):
    help = "Получить заказ по ID"
    
    def add_arguments(self, parser):
        parser.add_argument('color', type=str, help='Цвет')
        
    
    def handle(self, *args, **kwargs):
        color = kwargs['color']
        result = Product.objects.filter(name__contains=color).all()
        self.stdout.write(f'{result}')
        
