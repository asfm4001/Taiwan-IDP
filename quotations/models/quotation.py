from django.db import models
from decimal import Decimal, ROUND_HALF_UP
from quotations.autoNum import AutoNumberMixin
from quotations.models.company import Company
from quotations.models.client import Client
from quotations.models.product import Product
from quotations.models.order import Order, OrderProduct

class Quotation(AutoNumberMixin, models.Model):
    quotation_status_choice = {
        '': 'None',
        'draft': '草稿',
        'sent': '已報價',
        'accepted': '已接受',
        'rejected': '已拒絕',
    }
    number_prefix = 'Q'  # 流水號前綴
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
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