from django import forms
from datetime import date
from .models import Product

import logging

logger = logging.getLogger(__name__)

def get_choices():
    choices = [(0, "Добавить новый товар")]
    choices.extend(((product.pk, f'{product.name}') 
                 for product in Product.objects.all()))
    #logger.debug('Обновление списка')
    return choices
    
class ProductEditForm(forms.Form):
    name_select = forms.ChoiceField(choices=get_choices, 
                                    widget=forms.Select(attrs={'onchange': "window.location.href=this.value"}),
                                    label="Выбор товара для редактирования")
    
    name = forms.CharField(label='Наименование товара')
    description = forms.CharField(widget=forms.Textarea, label='Описание товара')
    price = forms.DecimalField(max_digits=10, decimal_places=2, label='Цена')    
    stock = forms.IntegerField(label='Остаток на складе')
    #image_name = forms.CharField(disabled=False, label='Изображение:', required=False)
    image = forms.ImageField(required=False, label='Загрузить изображение')
    
    def clean_stock(self):
        stock = int(self.cleaned_data['stock'])
        if  stock < 0:
            raise forms.ValidationError('Количество товара не может быть отрицательным')
        else:
            return stock
    
    
    def clean_price(self):
        price =  float(self.cleaned_data['price']) 
        if  price <= 0:
            raise forms.ValidationError('Цена товара не может быть менше/равно нулю')
        else:
            return price
    
        
        
