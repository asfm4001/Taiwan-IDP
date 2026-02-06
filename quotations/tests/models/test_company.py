from django.test import TestCase
from quotations.models import Company

def quick_create_company(num=1):
    """ Inter a number 'num' to generate multiple Companies."""
    for i in range(num):
        c = Company.objects.create(
            title = f'測試公司{i}',
            address = f'地址{i}',
            phone = f'(02)-12345{i}',
            fax = f'(02)-12345{i}',
            tax_code = f'12345{i}',
            icon = None,
            stamp = None,
            engineer_display = i
        )

class CompanyModelTest(TestCase):
    def test_create_company(self):
        quick_create_company(2)
        c0, c1 = Company.objects.all()[0], Company.objects.all()[1]

        self.assertEqual(c0.title, '測試公司0')
        self.assertEqual(c0.address, '地址0')
        self.assertEqual(c0.phone, '(02)-123450')
        self.assertEqual(c0.fax, '(02)-123450')
        self.assertEqual(c0.tax_code, '123450')
        self.assertFalse(c0.engineer_display)
        self.assertTrue(c1.engineer_display)