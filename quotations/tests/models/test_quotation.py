from django.test import TestCase
import pytest
from quotations.tests.factories import (
    QuotationFactory, 
    ProductFactory,
    QuotationProductFactory,
    SubProductFactory
)
from quotations.models import Order, OrderProduct, Quotation, Product

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
        self.assertEqual(self.q.subtotal, 400)

    def test_tax_amount(self):
        self.assertEqual(self.q.tax_amount, 40)

    def test_total_with_tax(self):
        self.assertEqual(self.q.total_with_tax, 440)

    def test_method_quotation_convert_to_order(self):
        o = self.q.convert_to_order()

        self.assertIsInstance(o, Order)

        field_list = [
            "company", "client", "name", "address", "area", 
            "tax_rate", "note", 

            "subtotal", "tax_amount", "total_with_tax"
            ]

        for field in field_list:
            self.assertEqual(getattr(o, field), getattr(self.q, field))
    
    def test_method_products_convert_to_order_product(self):
        o = self.q.convert_to_order()
        ops = OrderProduct.objects.filter(order=o)

        # 確定 轉換成訂單後僅有一筆資料
        self.assertEqual(ops.count(), 1)

        op = ops.get()

        self.assertEqual(op.product, self.p)
        self.assertEqual(op.quantity, self.qp.quantity)

    def test_method_clone_from_template_cloumn_is_correct(self):
        q_temp = QuotationFactory(tax_rate=10, is_template=True)

        new_q = q_temp.clone_from_template()
        self.assertIsInstance(new_q, Quotation)
        self.assertEqual(new_q.company, q_temp.company)
        self.assertEqual(new_q.client, q_temp.client)
        self.assertEqual(new_q.name, q_temp.name)
        self.assertEqual(new_q.address, q_temp.address)
        self.assertEqual(new_q.area, q_temp.area)
        self.assertEqual(new_q.tax_rate, q_temp.tax_rate)
        self.assertEqual(new_q.status, q_temp.status)
        self.assertEqual(new_q.note, q_temp.note)
        self.assertFalse(new_q.is_template)
    
    @pytest.mark.current
    def test_method_clone_from_template_products_is_correct(self):
        q_temp = QuotationFactory(tax_rate=10, is_template=True)

        p1_temp = ProductFactory(price=100, is_template=True)
        p2_temp = ProductFactory(price=200, is_template=True)

        SubProductFactory(product=p1_temp)
        SubProductFactory(product=p1_temp)
        SubProductFactory(product=p2_temp)

        QuotationProductFactory(quotation=q_temp, product=p1_temp, quantity=1)
        QuotationProductFactory(quotation=q_temp, product=p2_temp, quantity=2)

        # 將模板輸出成報價單
        new_q = q_temp.clone_from_template()

        temp_products = list(q_temp.products.all().order_by('id'))
        new_products = list(new_q.products.all().order_by('id'))

        # 檢核products數量是否相符
        self.assertEqual(len(temp_products), len(new_products))

        for temp_p, new_p in zip(temp_products, new_products):
            # 檢核 product不是同一筆資料
            self.assertNotEqual(temp_p.id, new_p.id)

            # column
            self.assertEqual(temp_p.name, new_p.name)
            self.assertEqual(temp_p.price, new_p.price)

            temp_subs = list(temp_p.subproducts.all().order_by('id'))
            new_subs = list(new_p.subproducts.all().order_by('id'))

            # 檢核subproducts數量是否相符
            self.assertEqual(len(temp_subs), len(new_subs))

            for temp_sb, new_sb in zip(temp_subs, new_subs):
                # 檢核 subproduct不是同一筆資料
                self.assertNotEqual(temp_sb.id, new_sb.id)

                # column
                self.assertEqual(temp_sb.name, new_sb.name)