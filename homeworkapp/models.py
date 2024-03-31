from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=254)
    created = models.DateField(auto_now_add=True)    
    
    def __str__(self):
        return f'Клиент: Имя: {self.name}, телефон:{self.phone}\n\t эл.почта: {self.email}\n\t адрес: {self.address}\n'
    

class Product(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    last_updated = models.DateField(auto_now=True)
    
    def __str__(self):
        return f'{self.name}, price: {self.price}, stock: {self.stock}\n'
    
    
class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    created = models.DateTimeField(auto_now_add=True)
    
    def total(self):
        return sum(product.price for product in self.products.all())
    
    def __str__(self):
        list_of_products = ', '.join(product.name for product in self.products.all())
        return f'Заказ:\tКлиент - {self.client.name}\n\tСписок товаров: {list_of_products},\n\tСтоимость заказа: {self.total()}\n\n'
    
    
    
    
