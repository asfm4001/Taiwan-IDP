from django.db import models
from django.contrib import admin
# Create your models here.

class Client(models.Model):
    client_name = models.CharField('客戶名稱', max_length=20)
    client_gui = models.CharField('客戶統編', max_length=8) # Government Uniform Invoice number
    client_phone = models.CharField('聯絡電話', max_length=10)
    # @admin.display(
    #     boolean=True,
    #     ordering='order_date',
    # )
    def __str__(self):
        return self.client_name
    
class Product(models.Model):
    product_name = models.CharField('施工品項', max_length=60)
    product_unit = models.IntegerField('單位')
    product_price = models.IntegerField('單價')

    def __str__(self):
        return self.product_name
    def calculate_amount(self):
        return self.product_unit*self.product_price

class Order(models.Model):
    status_list = {
        '未啟動',
        '進行中',  
        '已結案',
        '未結案'
    }
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    # product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    products = models.ManyToManyField(Product)
    order_address = models.CharField('施作地址', max_length=60)
    order_status = models.CharField('訂單狀態', max_length=10, default='未啟動')
    order_date = models.DateField('訂單日期')
    order_amount = models.IntegerField('總金額(已稅)', blank=True)
    contact_name =models.CharField('聯絡人姓名', max_length=10, blank=True)
    contact_phone =models.CharField('聯絡人電話', max_length=10, blank=True)
    note = models.TextField('備註', blank=True) # 可空白
    # @admin.display(
    #     boolean=True,
    #     ordering='order_date',
    # )
    def __str__(self):
        return self.order_address
    def calculate_total_amount(self):
        self.order_amount = 0
        for product in self.products.all():
            self.order_amount += product.calculate_amount()
        self.save()
        return self.order_amount
    # def order_status(self, status_list):
    #     return status_list[str(self.order_status)]

    