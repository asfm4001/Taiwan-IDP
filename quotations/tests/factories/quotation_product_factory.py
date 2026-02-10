import factory
from quotations.models import QuotationProduct
from quotations.tests.factories import QuotationFactory, ProductFactory

class QuotationProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = QuotationProduct

    quotation = factory.SubFactory(QuotationFactory)
    product = factory.SubFactory(ProductFactory)
    quantity = 1