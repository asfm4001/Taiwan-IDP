from django.test import TestCase
from quotations.tests.factories import (
    OrderFactory,
    ProductFactory,
    OrderProductFactory
)
class OrderProductTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.o = OrderFactory()
        cls.p = ProductFactory(price=100, is_active=True)
        cls.op = OrderProductFactory(
            order = cls.o, 
            product = cls.p,
            quantity = 2)

    def test_get_subtotal_with_quotation_and_products(self):
        self.assertEquals(self.op.get_subtotal, self.op.quantity * self.p.price)