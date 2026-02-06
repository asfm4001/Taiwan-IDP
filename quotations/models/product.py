from django.db import models

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