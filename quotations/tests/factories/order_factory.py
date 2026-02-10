import factory
from decimal import Decimal
from quotations.models import Order
from quotations.tests.factories import CompanyFactory, ClientFactory
class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Order

    company = factory.SubFactory(CompanyFactory)
    client = factory.SubFactory(ClientFactory)
    name = '測試施作'
    address = '測試地址'
    contact_name = '測試聯絡人'
    area = 100
    tax_rate = Decimal('5')
    status = 'pending'
    note = '測試備註'