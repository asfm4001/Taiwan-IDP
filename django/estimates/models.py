from django.db import models
from django.contrib import admin
from decimal import Decimal, ROUND_HALF_UP
from estimates.autoNum import AutoNumberMixin

class Client(models.Model):
    name = models.CharField('客戶名稱', max_length=20)
    gui = models.CharField('客戶統編', max_length=8, blank=True, null=True) # Government Uniform Invoice number
    phone = models.CharField('聯絡電話', max_length=10, blank=True, null=True)
    # @admin.display(
    #     boolean=True,
    #     ordering='order_date',
    # )
    class Meta:
        verbose_name = '業主'               # 自定義後台table name
        verbose_name_plural = '業主管理'    # 複數table name 
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField('施工品項', max_length=60)
    price = models.IntegerField('單價')
    is_active = models.BooleanField('啟用狀態', default=True)
    class Meta:
        verbose_name = '工作項目'
        verbose_name_plural = '工作項目'
    def __str__(self):
        return self.name

class SubProduct(models.Model):
    product = models.ForeignKey(Product, related_name='subproducts', on_delete=models.CASCADE)
    name = models.CharField('子工作項目', max_length=120)
    def __str__(self):
        return self.name

class Quotation(AutoNumberMixin, models.Model):
    quotation_status_choice = {
        '': 'None',
        'draft': '草稿',
        'sent': '已報價',
        'accepted': '已接受',
        'rejected': '已拒絕',
    }
    number_prefix = 'Q'  # 流水號前綴
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='QuotationProduct')

    name = models.CharField('施作名稱', max_length=100, null=True)
    number = models.CharField('報價單編號', max_length=20, unique=True, editable=False)
    address = models.CharField('施作地址', max_length=100)
    contact_name = models.CharField('聯絡人姓名', max_length=20, blank=True, null=True)
    # contact_phone = models.CharField('聯絡人電話', max_length=10, blank=True)
    
    # order_status = models.CharField('報價單狀態', max_length=10, default='未啟動')
    area = models.FloatField('面積', blank=True, null=True)
    created_date = models.DateField('訂單日期', auto_now_add=True)
    tax_rate = models.DecimalField(max_digits=9, decimal_places=0, default=5)
    status = models.CharField('狀態', max_length=20, choices=quotation_status_choice, blank=True, default='')
    note = models.TextField('備註', blank=True, null=True)
    class Meta:
            verbose_name = '報價單'
            verbose_name_plural = '報價單'
    def __str__(self):
        return self.number
    
    @property
    def subtotal(self):
        return sum(qp.get_subtotal for qp in self.quotationproduct_set.all())

    @property
    def tax_amount(self):
        return (self.subtotal * (self.tax_rate/(Decimal('100')))).quantize(Decimal('1'), rounding=ROUND_HALF_UP)

    @property
    def total_with_tax(self):
        return self.subtotal + self.tax_amount
    
    def convert_to_order(self):
        # 1. create order 
        order = Order.objects.create(
            client = self.client,
            name = self.name,
            address = self.address,
            area = self.area,
            contact_name = self.contact_name,
            tax_rate = self.tax_rate,
            note = self.note
        )
        # 2. create orderItems
        for item in self.quotationproduct_set.all():
            OrderProduct.objects.create(
                order = order,
                product = item.product,
                quantity = item.quantity
            )
        return order

class QuotationProduct(models.Model):
    quotation = models.ForeignKey('Quotation', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField('數量', default=1)

    def __str__(self):
            return f"{self.quotation} - {self.product} x {self.quantity}"

    @property
    def get_subtotal(self):
        return self.quantity * self.product.price

class Order(AutoNumberMixin, models.Model):
    order_status_choice = {
        'pending': '未處理',
        # 'confirmed': '已確認',
        'processing': '處理中',
        # '': '施工中',
        'completed': '已完成',
        'cancelled': '已取消',
    }
    number_prefix = 'Order'
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderProduct')

    name = models.CharField('工作名稱', max_length=100, null=True)
    number = models.CharField('訂單編號', max_length=20, unique=True, editable=False)
    address = models.CharField('施作地址', max_length=100)
    # status = models.CharField('訂單狀態', max_length=10, default='未啟動')
    area = models.FloatField('面積', blank=True, null=True)
    contact_name =models.CharField('聯絡人姓名', max_length=10, blank=True, null=True)
    created_date = models.DateField('訂單日期', auto_now_add=True)
    tax_rate = models.DecimalField(max_digits=9, decimal_places=0, default=5)
    status = models.CharField('狀態', max_length=20, choices=order_status_choice, blank=True, default='pending')
    # contact_phone =models.CharField('聯絡人電話', max_length=10, blank=True)
    note = models.TextField('備註', blank=True, null=True) # 可空白
    # @admin.display(
    #     boolean=True,
    #     ordering='order_date',
    # )
    class Meta:
        verbose_name = '訂單'
        verbose_name_plural = '訂單'
    def __str__(self):
        return self.address
    @property
    def subtotal(self):
        return sum(op.get_subtotal for op in self.orderproduct_set.all())

    @property
    def tax_amount(self):
        return (self.subtotal * (self.tax_rate/(Decimal('100')))).quantize(Decimal('1'), rounding=ROUND_HALF_UP)

    @property
    def total_with_tax(self):
        return self.subtotal + self.tax_amount

class OrderProduct(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField('數量', default=1)

    def __str__(self):
        return f"{self.order} - {self.product} x {self.quantity}"

    @property
    def get_subtotal(self):
        return self.quantity * self.product.price
