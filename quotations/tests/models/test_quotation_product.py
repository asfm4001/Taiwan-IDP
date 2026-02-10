from django.test import TestCase
from quotations.tests.factories import (
    QuotationFactory,
    ProductFactory,
    QuotationProductFactory
)

class QuotationProductTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.q = QuotationFactory()
        cls.p = ProductFactory(price=100, is_active=True)
        cls.qp = QuotationProductFactory(
            quotation = cls.q, 
            product = cls.p,
            quantity = 2)

    def test_get_subtotal_with_quotation_and_products(self):
        self.assertEqual(self.qp.get_subtotal, self.qp.quantity * self.p.price)
