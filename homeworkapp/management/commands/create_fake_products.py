from django.core.management.base import BaseCommand
from homeworkapp.models import Product, Client, Order, Category
from random import choice, randint, random, choices
from datetime import date, timedelta
class Command(BaseCommand):
    help = "Заполнить базу товарами"
    
    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Количество товаров')
        
    
    def handle(self, *args, **kwargs):
        furniture = {
            'Мебель для кухни': ['кухонный уголок', 'обеденный стол', 'обеденный стул', 'кухонный фартук'],
            'Мебель для гостиной' : [ 'стенкa', 'витрина', 'буфет', 'комод', 'тумба под ТВ',
                                     'консоль', 'журнальный столик', 'сервировочный столик',                                      
                                     'вешалка', 'зеркало', 'винный бар', 'цветочница', 'газетница', ],
            'Мебель для спальни':['кровать', 'матрас', 'шкаф', 'прикроватная тумбочка', 'туалетный столик'],
            'Мягкая мебель': ['диван', 'угловой диван', 'модульный диван', 'раскладное кресло', 'кресло', 'пуф', 'банкетка']
        }
        color = 'черный белый красный зеленый синий желтый'
        
        LOREM = """Occaecat adipisicing ipsum exercitation non est laboris cillum culpa pariatur. Nostrud mollit dolor aliqua eiusmod proident ad est pariatur reprehenderit irure nostrud voluptate occaecat. Quis sit qui Lorem consequat culpa sint tempor labore commodo velit. Ex culpa labore consequat in sint aliquip commodo. Qui dolor fugiat nulla minim id magna et. Dolor laboris fugiat eiusmod enim proident qui nisi esse elit proident esse magna aliqua proident. Minim consequat incididunt Lorem nostrud magna ut elit consequat fugiat commodo veniam labore amet est.                   Adipisicing in tempor minim cillum est cillum anim reprehenderit culpa dolor ea esse eiusmod consectetur. Ut enim est sunt dolor. Anim do amet nulla exercitation. Ipsum excepteur ad reprehenderit officia enim et sint. Aliqua minim sint ea reprehenderit sint.
            Eu est voluptate mollit sunt commodo mollit enim ut minim amet ullamco incididunt eiusmod nisi. Nisi exercitation do dolore amet nisi fugiat ex do id quis. Elit ullamco esse id veniam ad nostrud irure. Pariatur Lorem fugiat tempor velit irure velit dolor ex. Labore do qui qui magna exercitation veniam eu. Cillum velit consequat tempor ex ea dolore ipsum nisi. Magna irure ut adipisicing voluptate.
            Adipisicing nisi minim labore dolor ea labore dolor. In dolor non elit laborum do quis do dolor Lorem et commodo aliquip. Fugiat deserunt excepteur tempor eu aliquip excepteur ad. Esse pariatur ex ipsum minim cillum nostrud enim voluptate. Excepteur ad Lorem quis dolor excepteur proident pariatur et laboris nisi sit excepteur ad. Officia laborum amet laborum dolore est ullamco aliqua elit nostrud ad. Cupidatat ullamco fugiat reprehenderit culpa ad exercitation.
            """
            
        # for cat in furniture.keys():
        #     Category(name=cat).save()
        
        categories = Category.objects.all()
        
        count = kwargs['count']
        for i in range(count):
            category_=choice(categories)
            discount_ = 1
            if choice((True, False)):
                discount_= random()
            
            
            product = Product(category=category_,
                              name=f'{choice(furniture.get(category_.name))}',
                              color=f'{choice(color)}',
                              description= " ".join(choices(LOREM.split(), k=100)),
                              price=randint(1000, 10000),
                              stock=randint(1,100),
                              rating=randint(1,5),
                              last_updated=date.today() - timedelta(days=randint(30, 365)),
                              discount=discount_,
                              )
            product.save()
            self.stdout.write(f'{product}')
        
