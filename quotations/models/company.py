from django.db import models

class Company(models.Model):
    title = models.CharField('公司名稱', max_length=40)
    address = models.CharField('地址', max_length=100, blank=True, null=True)
    phone = models.CharField('電話', max_length=20, blank=True, null=True)
    fax = models.CharField('傳真', max_length=20, blank=True, null=True)
    tax_code = models.CharField('統編', max_length=20, blank=True, null=True)
    icon = models.CharField(max_length=255, blank=True, null=True)
    stamp = models.CharField(max_length=255, blank=True, null=True)
    engineer_display = models.BooleanField('技師顯示', default=True)
    class Meta:
        verbose_name = '公司'
        verbose_name_plural = '公司管理'
    def __str__(self):
        return self.title