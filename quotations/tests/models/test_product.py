from django.test import TestCase
from quotations.models import Product

def quick_create_product(num=1):
    """ Inter a number 'num' to generate multiple Companies."""
    for i in range(num):
        c = Product.objects.create(
            name = f'測試工作項目{i}',
            price = i,
            is_active = i
        )

class ProductModelTest(TestCase):
    def test_create_product(self):
        quick_create_product(2)
        p0, p1 = Product.objects.all()[0], Product.objects.all()[1]

        self.assertEqual(p0.name, '測試工作項目0')
        self.assertEqual(p0.price, 0)
        self.assertFalse(p0.is_active)
        self.assertEqual(p1.name, '測試工作項目1')
        self.assertEqual(p1.price, 1)
        self.assertTrue(p1.is_active)