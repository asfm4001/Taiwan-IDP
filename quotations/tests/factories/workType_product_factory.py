import factory
from quotations.models import WorkTypeProduct
from quotations.tests.factories import WorkTypeFactory, ProductFactory

class WorkTypeProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = WorkTypeProduct

    worktype = factory.SubFactory(WorkTypeFactory)
    product = factory.SubFactory(ProductFactory)
    quantity = 1