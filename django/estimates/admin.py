from django.contrib import admin
from .models import Client, Order, Product
# Register your models here.

class ClientAdmin(admin.ModelAdmin):
    fieldsets = [
        ('客戶資料', {
            'fields': [('client_name', 'client_phone'), 'client_gui'],
            # "classes": ["collapse"]
        })
    ]
    search_fields = ["client_name"]
    list_display = ["client_name", "client_phone", "client_gui"]
    
class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        ('施工品項', {
            'fields': ['product_name', ('product_unit', 'product_price')]
        })
    ]
    list_display = ['product_name']


class OrderAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            "fields": ['client'],
            # "classes": ["collapse"]
            }),
        ("訂單資訊", {
            "fields": [('order_address', 'order_date'), 'order_status', 'order_amount'],
            }),
        ("聯絡資訊", {
            "fields": [('contact_name', 'contact_phone'), 'note'],
            }),
        (None, {
            "fields": ['products'],
            # "classes": ["collapse"]
            }),
        
    ]
    # inlines = [ClientInline]
    search_fields = ['order_address']
    # date_hierarchy = 'order_date'     # 日期分類
    list_display = ["order_address", "order_status", "order_date", 'order_amount', 'contact_name', 'contact_phone']
    list_filter = ['order_status']
    view_on_site = True
    ordering = ['order_date']

admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)