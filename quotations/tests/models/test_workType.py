from django.test import TestCase
import pytest
from quotations.tests.factories import (
    WorkTypeFactory,
    ProductFactory,
    WorkTypeProductFactory,
    SubProductFactory
)
from quotations.models import Quotation

class WorkTypeTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.w = WorkTypeFactory()
    
    def test_clone_from_template_cloumn_is_correct(self):
        new_q = self.w.clone_from_template()
        self.assertIsInstance(new_q, Quotation)
        self.assertEqual(new_q.company, self.w.company)
        self.assertEqual(new_q.client, self.w.client)
        self.assertEqual(new_q.work_type, self.w)
        self.assertEqual(new_q.name, self.w.name)
        self.assertEqual(new_q.note, self.w.note)

    def test_clone_from_template_product_is_correct(self):
        p1 = ProductFactory(price=100)
        p2 = ProductFactory(price=200)

        SubProductFactory(product=p1)
        SubProductFactory(product=p1)
        SubProductFactory(product=p2)

        WorkTypeProductFactory(worktype=self.w, product=p1, quantity=1)
        WorkTypeProductFactory(worktype=self.w, product=p2, quantity=2)

        new_q = self.w.clone_from_template()

        temp_products = list(self.w.products.all().order_by('id'))
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