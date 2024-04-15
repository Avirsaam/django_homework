from django.contrib import admin
from .models import Order, Product, Client
# Register your models here.

@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(stock=0)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'stock', 'price', ]
    list_per_page = 20    
    ordering = ['-stock', 'name']        
    search_fields = ['name', 'description']
    search_help_text = 'Поиск по названию/описанию'
    actions = [reset_quantity]
    readonly_fields = ['last_updated']
    

class ClientAdmin(admin.ModelAdmin):
    list_display = ['name']
    #ordering = ['surname']
    search_fields = ['name']    
    search_help_text = 'Поиск по имени/фамилии'
    readonly_fields = ['created']

class OrdersAdmin(admin.ModelAdmin):
    list_display = ['created', 'get_name', 'ordered_items',  'total']
    ordering = ['-created']
    list_filter = ['created']
    search_fields = ['get_name']
    search_help_text = 'Поиск по имени/фамилии'
    readonly_fields = ['created']
    
    def get_name(self, obj):
        return obj.client.name
    get_name.admin_order_field = 'client-name'
    get_name.short_description = 'Имя клиента'
    
    filter_horizontal=['products']
    fieldsets = [
        (
            None,
            {
                "fields": ['client', 'created', 'products'],
            },
        ),        
    ]
    

admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrdersAdmin)
