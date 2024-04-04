from django.core.management.base import BaseCommand
from homeworkapp.models import Product, Client, Order
from random import choice, randint
from datetime import date, timedelta
class Command(BaseCommand):
    help = "Заполнить базу клиентами"
    
    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Количество клиентов')
        
    
    def handle(self, *args, **kwargs):
        names = ['Иван', 'Пётр', 'Сергей', 'Николай', 'Константин', 'Олег']
        surnames = ['Иванов', 'Петров', 'Сидоров', 'Толстой', 'Пушкин', 'Некрасов', 'Тургенев', 'Лермонтов']
        
        count = kwargs['count']
        for i in range(count):
            client = Client(name=f'{choice(names)} {choice(surnames)}', 
                            email=f'email{i}@example.com', 
                            phone=f'+7-{randint(900, 990)}-{randint(100,999)}-{randint(10,99)}-{randint(10,99)}',
                            address=f'Адрес {i}',
                            created=date(2014, 1, 1) + timedelta(days=randint(1, 3650)))
            
            client.save()
            self.stdout.write(f'{client}')
        
