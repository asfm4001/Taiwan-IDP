from django.test import TestCase
from quotations.tests.factories import (
    OrderFactory, 
    ProductFactory,
    OrderProductFactory
)

class OrderTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.o = OrderFactory(tax_rate=10)
        cls.p = ProductFactory(price=200)
        cls.op = OrderProductFactory(
            order = cls.o,
            product = cls.p,
            quantity = 2
        )

    def test_create_order_has_company_and_client(self):
        # smoke test(測試關聯，不測試邏輯)
        self.assertIsNotNone(self.o.company)
        self.assertIsNotNone(self.o.client)
        
    def test_subtotal_with_quotationproducts(self):
        self.assertEqual(self.o.subtotal, self.op.quantity * self.p.price)

    def test_tax_amount(self):
        self.assertEqual(self.o.tax_amount, self.o.subtotal * self.o.tax_rate / 100)

    def test_total_with_tax(self):
        self.assertEqual(self.o.total_with_tax, self.o.subtotal + self.o.tax_amount)