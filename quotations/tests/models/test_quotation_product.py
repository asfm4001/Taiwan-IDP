from django.test import TestCase
from quotations.models import Quotation, Product, QuotationProduct
from quotations.tests.factories import (
    create_quotation, 
    create_product, 
    add_product_to_quotation
)
class QuotationProductTest(TestCase):
    def test_get_subtotal_with_quotation_and_products(self):
        q = create_quotation()
        p = create_product(name='測試工作項目', price=100, is_active=True)
        qp = add_product_to_quotation(q, p, 2)
        self.assertEquals(qp.get_subtotal, 200)
