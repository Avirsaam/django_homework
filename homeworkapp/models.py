from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=64)
    second_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=254)
    created = models.DateField()  
    
    @property
    def name(self):
        return f'{self.second_name.capitalize()} {self.first_name.capitalize()}'
        
    def __str__(self):
        return f'{self.name}, телефон:{self.phone}\n'
    
    def get_total_orders(self):
        return Order.objects.filter(client=self).count()

class Category(models.Model):
    name = models.CharField(max_length=64)
    
    def __str__(self):
        return f'{self.name}'

class Product(models.Model):
    name = models.CharField(max_length=254)
    color = models.CharField(max_length=64)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    last_updated = models.DateField()
    image = models.ImageField(blank=True)
    rating = models.IntegerField(default=4)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    discount = models.FloatField(default=1)
    
    def __str__(self):
        return f'{self.name.capitalize()}, price: {self.price}, stock: {self.stock}\n'
    
    def isSale(self):
        return self.discount != 1
    
    def price_discount(self):
        return f'{float(self.price) * self.discount:.2f}'
    
    def get_rating_stars(self):
        return range(self.rating)
    
    
class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    created = models.DateTimeField()  
    
    def client_name(self):
        return self.client.name
    
    def ordered_items(self):
        return self.products.all().count() 
    
    def total(self):
        return sum(product.price for product in self.products.all())
    
    def __str__(self):
        list_of_products = ', '.join(product.name for product in self.products.all())
        return f'Заказ:\tКлиент - {self.client.name}\n\tСписок товаров: {list_of_products},\n\tСтоимость заказа: {self.total()}\n\n'
        
    
    
    
    
