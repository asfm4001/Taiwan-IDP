import factory
from quotations.models import WorkType
from quotations.tests.factories.company_factory import CompanyFactory
from quotations.tests.factories.client_factory import ClientFactory

class WorkTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = WorkType

    company = factory.SubFactory(CompanyFactory)
    client = factory.SubFactory(ClientFactory)

    name = '測試工作項目類型'
    note = '測試備註'