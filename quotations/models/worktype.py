from django.db import models

class WorkType(models.Model):
    name = models.CharField('工作項目類型', max_length=50)
    products = models.ManyToManyField('quotations.Product', through='WorkTypeProduct')
    note = models.TextField('備註', blank=True, null=True)

    class Meta:
        verbose_name = '工作項目類型'
        verbose_name_plural = '工作項目類型'

    def __str__(self):
        return self.name

class WorkTypeProduct(models.Model):
    worktype = models.ForeignKey('quotations.WorkType', on_delete=models.CASCADE)
    product = models.ForeignKey('quotations.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField('數量', default=1)

    def __str__(self):
            return f"{self.worktype} - {self.product} x {self.quantity}"

    @property
    def get_subtotal(self):
        return self.quantity * self.product.price