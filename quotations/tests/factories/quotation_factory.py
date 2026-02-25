import factory
from decimal import Decimal
from quotations.models import Quotation
from quotations.tests.factories.company_factory import CompanyFactory
from quotations.tests.factories.client_factory import ClientFactory

class QuotationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Quotation

    company = factory.SubFactory(CompanyFactory)
    client = factory.SubFactory(ClientFactory)

    name = '測試施作'
    address = '測試地址'
    area = 100
    tax_rate = Decimal('5')
    status = 'draft'
    note = '測試備註'