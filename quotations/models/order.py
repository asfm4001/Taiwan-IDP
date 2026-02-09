from django.db import models
from decimal import Decimal, ROUND_HALF_UP
from quotations.autoNum import AutoNumberMixin
from quotations.models import Company, Client, Product

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
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
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