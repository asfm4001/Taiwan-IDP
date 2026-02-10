import factory
from quotations.models import OrderProduct
from quotations.tests.factories import OrderFactory, ProductFactory

class OrderProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = OrderProduct

    order = factory.SubFactory(OrderFactory)
    product = factory.SubFactory(ProductFactory)
    quantity = 1