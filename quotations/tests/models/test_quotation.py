from django.test import TestCase
from quotations.tests.factories import (
    QuotationFactory, 
    ProductFactory,
    QuotationProductFactory
)
from quotations.models import Order, OrderProduct

class QuotationTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.q = QuotationFactory(tax_rate=10)
        cls.p = ProductFactory(price=200)
        cls.qp = QuotationProductFactory(
            quotation = cls.q,
            product = cls.p,
            quantity = 2
        )

    def test_create_quotation_has_company_and_client(self):
        # smoke test(測試關聯，不測試邏輯)
        self.assertIsNotNone(self.q.company)
        self.assertIsNotNone(self.q.client)
        
    def test_subtotal_with_quotationproducts(self):
        self.assertEqual(self.q.subtotal, self.qp.quantity * self.p.price)

    def test_tax_amount(self):
        self.assertEqual(self.q.tax_amount, self.q.subtotal * self.q.tax_rate / 100)

    def test_total_with_tax(self):
        self.assertEqual(self.q.total_with_tax, self.q.subtotal + self.q.tax_amount)

    def test_method_quotation_convert_to_order(self):
        o = self.q.convert_to_order()

        self.assertIsInstance(o, Order)
        self.assertEqual(o.company, self.q.company)
        self.assertEqual(o.client, self.q.client)
        self.assertEqual(o.name, self.q.name)
        self.assertEqual(o.address, self.q.address)
        self.assertEqual(o.area, self.q.area)
        self.assertEqual(o.contact_name, self.q.contact_name)
        self.assertEqual(o.tax_rate, self.q.tax_rate)
        self.assertEqual(o.note, self.q.note)
        self.assertEqual(o.subtotal, self.q.subtotal)
        self.assertEqual(o.tax_amount, self.q.tax_amount)
        self.assertEqual(o.total_with_tax, self.q.total_with_tax)
    
    def test_products_convert_to_order_product(self):
        o = self.q.convert_to_order()
        op = OrderProduct.objects.filter(order=o).first()

        self.assertEqual(op.product, self.p)
        self.assertEqual(op.quantity, self.qp.quantity)