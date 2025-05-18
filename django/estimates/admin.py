from django.contrib import admin
from .models import Client, Order, Product, OrderProduct, Quotation, QuotationProduct
# Register your models here.

class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    extra = 1

class QuotationProductInline(admin.TabularInline):
    model = QuotationProduct
    extra = 1

class ClientAdmin(admin.ModelAdmin):
    fieldsets = [
        ('客戶資料', {
            'fields': [('name', 'phone'), 'gui'],
            # "classes": ["collapse"]
        })
    ]
    search_fields = ["name"]
    list_display = ["name", "phone", "gui"]
    
class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        ('施工品項', {
            'fields': ['name', 'price']
        })
    ]
    list_display = ['name']

class QuotationAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            "fields": ['client'],
            # "classes": ["collapse"]
            }),
        ("訂單資訊", {
            "fields": ['name', ('address', 'created_date'), 'area'],
            }),
        ("聯絡資訊", {
            "fields": [('contact_name'), 'note'],
            }),
    ]
    inlines = [QuotationProductInline]
    search_fields = ['address']
    list_display = ["address", "created_date", 'contact_name']
    view_on_site = True
    ordering = ['created_date']


class OrderAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            "fields": ['client'],
            # "classes": ["collapse"]
            }),
        ("訂單資訊", {
            "fields": [('address', 'created_date'), 'status'],
            }),
        ("聯絡資訊", {
            "fields": [('contact_name', 'contact_phone'), 'note'],
            }),
    ]
    inlines = [OrderProductInline]
    search_fields = ['address']
    # date_hierarchy = 'order_date'     # 日期分類
    list_display = ["address", "status", "created_date", 'contact_name', 'contact_phone']
    list_filter = ['status']
    view_on_site = True
    ordering = ['created_date']

admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Quotation, QuotationAdmin)