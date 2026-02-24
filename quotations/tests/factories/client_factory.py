import factory
from quotations.models import Client

class ClientFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Client

    name = factory.Sequence(lambda n: f"測試客戶 {n}")
    gui = '1234567'
    phone = '02-2345678#1234'
    contact_name = '測試聯絡人'
    contact_phone = '(02)-23456789#12345'