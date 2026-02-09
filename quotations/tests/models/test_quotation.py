from django.test import TestCase
from quotations.tests.factories import (
    create_quotation,
    create_product,
    add_product_to_quotation
)
from quotations.models import Order, OrderProduct

class QuotationTest(TestCase):
    def setUp(self):
        self.q = create_quotation(tax_rate=10)
        self.p = create_product(price=200)
        self.qp = add_product_to_quotation(self.q, self.p, 2)
        self.o = self.q.convert_to_order()

    def test_create_quotation_has_company_and_client(self):
        # smoke test(測試關聯，不測試邏輯)
        self.assertIsNotNone(self.q.company)
        self.assertIsNotNone(self.q.client)
        
    def test_subtotal_with_quotationproducts(self):
        self.assertEqual(self.q.subtotal, 400)


    def test_tax_amount(self):
        self.assertEqual(self.q.tax_amount, 40)

    def test_total_with_tax(self):
        self.assertEqual(self.q.total_with_tax, 440)

    def test_method_quotation_convert_to_order(self):
        self.assertIsInstance(self.o, Order)
        self.assertEqual(self.o.company, self.q.company)
        self.assertEqual(self.o.client, self.q.client)
        self.assertEqual(self.o.name, self.q.name)
        self.assertEqual(self.o.address, self.q.address)
        self.assertEqual(self.o.area, self.q.area)
        self.assertEqual(self.o.contact_name, self.q.contact_name)
        self.assertEqual(self.o.tax_rate, self.q.tax_rate)
        self.assertEqual(self.o.note, self.q.note)
        self.assertEqual(self.o.subtotal, self.q.subtotal)
        self.assertEqual(self.o.tax_amount, self.q.tax_amount)
        self.assertEqual(self.o.total_with_tax, self.q.total_with_tax)
    
    def test_products_convert_to_order_product(self):
        op = OrderProduct.objects.get(order=self.o)
        self.assertEqual(op.product, self.p)
        self.assertEqual(op.quantity, self.qp.quantity)