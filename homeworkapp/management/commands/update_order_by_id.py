from django.core.management.base import BaseCommand
from homeworkapp.models import Client, Product, Order
from random import choice, randint

class Command(BaseCommand):
    help = "Добавить/удалить товары в заказ"
    
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Order ID')
        
    
    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        order = Order.objects.filter(pk=pk).first()
        if order is not None:
            self.stdout.write(f'Заказ до изменения:\n{order}')
            
            product_count = order.products.count()
            
            if product_count != 0 and choice((0,1)):                
                for _ in range(randint(1, product_count)):
                    product = choice(order.products.all())
                    self.stdout.write(f'Удаляем: {product.name}\n')
                    order.products.remove(product)            
            else:                                
                products = Product.objects.all()
                for _ in range(randint(1,5)):
                    product = choice(products)
                    self.stdout.write(f'Добавлено: {product.name}\n')
                    order.products.add(product)
                order.save()                    
                
            self.stdout.write(f'Заказ после изменения:\n{order}')
        else:
            self.stdout.write('Заказа с таким номером не существует')
        
