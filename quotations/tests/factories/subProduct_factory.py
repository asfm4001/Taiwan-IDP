import factory
from quotations.models import SubProduct
from quotations.tests.factories import ProductFactory

class SubProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = SubProduct

    product = factory.SubFactory(ProductFactory)
    name = '測試子項目'