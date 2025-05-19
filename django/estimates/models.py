from django.db import models
from django.contrib import admin
from decimal import Decimal
# Create your models here.

class Client(models.Model):
    name = models.CharField('客戶名稱', max_length=20)
    gui = models.CharField('客戶統編', max_length=8) # Government Uniform Invoice number
    phone = models.CharField('聯絡電話', max_length=10)
    # @admin.display(
    #     boolean=True,
    #     ordering='order_date',
    # )
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '業主'               # 自定義後台table name
        verbose_name_plural = '業主管理'    # 複數table name 
    
class Product(models.Model):
    name = models.CharField('施工品項', max_length=60)
    price = models.IntegerField('單價')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '工作項目'
        verbose_name_plural = '工作項目'

class Order(models.Model):
    status_list = {
        '未啟動',
        '進行中',  
        '已結案',
        '未結案'
    }
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderProduct')
    address = models.CharField('施作地址', max_length=60)
    status = models.CharField('訂單狀態', max_length=10, default='未啟動')
    created_date = models.DateField('訂單日期')
    # order_amount = models.IntegerField('總金額(已稅)', blank=True)
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2, default=5.00)
    contact_name =models.CharField('聯絡人姓名', max_length=10, blank=True)
    contact_phone =models.CharField('聯絡人電話', max_length=10, blank=True)
    note = models.TextField('備註', blank=True) # 可空白
    # @admin.display(
    #     boolean=True,
    #     ordering='order_date',
    # )
    def __str__(self):
        return self.address
    @property
    def subtotal(self):
        return sum(op.get_subtotal for op in self.orderproduct_set.all())

    @property
    def tax_amount(self):
        return self.subtotal * (self.tax_rate / Decimal('100.00'))

    @property
    def total_with_tax(self):
        return self.subtotal + self.tax_amount
    class Meta:
        verbose_name = '訂單'
        verbose_name_plural = '訂單'

class Quotation(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='QuotationProduct')

    name = models.CharField('施作名稱', max_length=20)
    contact_name = models.CharField('聯絡人姓名', max_length=10)
    # contact_phone = models.CharField('聯絡人電話', max_length=10, blank=True)
    address = models.CharField('施作地址', max_length=100)
    # order_status = models.CharField('報價單狀態', max_length=10, default='未啟動')
    area = models.FloatField('面積')
    created_date = models.DateField('訂單日期')
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2, default=5.00)
    note = models.TextField('備註', blank=True)

    def __str__(self):
        return self.address
    
    @property
    def subtotal(self):
        return sum(qp.get_subtotal for qp in self.quotationproduct_set.all())

    @property
    def tax_amount(self):
        return self.subtotal * (self.tax_rate / Decimal('100.00'))

    @property
    def total_with_tax(self):
        return self.subtotal + self.tax_amount
    class Meta:
        verbose_name = '報價單'
        verbose_name_plural = '報價單'

class OrderProduct(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField('數量', default=1)

    @property
    def get_subtotal(self):
        return self.quantity * self.product.price

    def __str__(self):
        return f"{self.order} - {self.product} x {self.quantity}"
    
class QuotationProduct(models.Model):
    quotation = models.ForeignKey('Quotation', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField('數量', default=1)

    @property
    def get_subtotal(self):
        return self.quantity * self.product.product_price

    def __str__(self):
        return f"{self.quotation} - {self.product} x {self.quantity}"
