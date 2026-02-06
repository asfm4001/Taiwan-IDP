from django.db import models

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