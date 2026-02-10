import factory
from quotations.models import Company

class CompanyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Company

    title = '測試公司'
    address = '測試地址'
    phone = '(02)-23456789'
    fax = '(02)-23456789'
    tax_code = '12345678'
    icon = None
    stamp = None
    engineer_display =  True