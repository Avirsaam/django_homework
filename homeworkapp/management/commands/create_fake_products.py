from django.core.management.base import BaseCommand
from homeworkapp.models import Product, Client, Order
from random import choice, randint
from datetime import date, timedelta
class Command(BaseCommand):
    help = "Заполнить базу товарами"
    
    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Количество товаров')
        
    
    def handle(self, *args, **kwargs):
        names = 'диван стул стол шкаф шифоньер трельяж секретер'
        color = 'черный белый красный зеленый синий желтый'
                
        count = kwargs['count']
        for i in range(count):
            product = Product(name=f'{choice(color.split())} {choice(names.split())}',
                              description='Sunt ex consequat irure aliquip ea sunt et.Sit consequat commodo dolore magna occaecat est.',
                              price=randint(1000, 10000),
                              stock=randint(1,100),
                              last_updated=date.today() - timedelta(days=randint(30, 365))
                              )
            product.save()
            self.stdout.write(f'{product}')
        
