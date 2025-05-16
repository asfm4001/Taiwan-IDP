from django.test import TestCase
from estimates.models import Client, Product, Quotation, QuotationProduct
from datetime import date

def quick_create_client(nums=1):
    for i in range(nums):
        c = Client.objects.create(
            client_name = f'測試客戶名{i+1}', 
            client_gui = '12345678', 
            client_phone = '0912345678'
        )
    return Client.objects.all()

def quick_create_product(nums=1):
    for i in range(nums):
        p = Product.objects.create(
            product_name = f'測試工作項目名稱{i+1}',
            product_price = 1000
        )
    return Product.objects.all()

def quick_create_quotation(client, nums=1):
    for i in range(nums):
        q = Quotation.objects.create(
            client = client,
            name = f'測試報價單名稱{i+1}', 
            contact_name = '測試聯絡人名稱', 
            address='測試施作地址', 
            area = 1562.52, 
            created_date = date.today(), 
            tax_rate = 5
        )
    return Quotation.objects.all()

def quick_create_quotationProduct(q, p):
    return QuotationProduct.objects.create(
            quotation = q,
            product = p,
            quantity = 1
        )

class ClientTest(TestCase):
    def test_create_client(self):
        c = Client.objects.create(
            client_name = '測試客戶名', 
            client_gui = '12345678', 
            client_phone = '0912345678'
        )
        self.assertEqual(c.client_name, '測試客戶名')
        self.assertEqual(c.client_gui, '12345678')
        self.assertEqual(c.client_phone, '0912345678')

class ProductTest(TestCase):
    def test_create_product(self):
        p = Product.objects.create(
            product_name = '測試工作項目名稱',
            product_price = 666
        )
        self.assertEqual(p.product_name, '測試工作項目名稱')
        self.assertEqual(p.product_price, 666)

class QuotationTest(TestCase):
    def test_create_quotation(self):
        c = quick_create_client()[0]
        q = Quotation.objects.create(
            client = c,
            name='測試報價單名稱', 
            contact_name='測試聯絡人名稱', 
            address='測試施作地址', 
            area=1562.52, 
            created_date=date.today(), 
            tax_rate=5
        )

        self.assertEqual(q.name, '測試報價單名稱')
        self.assertEqual(q.contact_name, '測試聯絡人名稱')
        self.assertEqual(q.address, '測試施作地址')
        self.assertIs(q.area, 1562.52)
        self.assertEqual(q.created_date, date.today())
        self.assertIs(q.tax_rate, 5)
    
    def test_subtotal(self):
        c = quick_create_client()[0]
        q = quick_create_quotation(c)[0]
        p = quick_create_product(2)
        qp1 = quick_create_quotationProduct(q, p[0])
        qp2 = quick_create_quotationProduct(q, p[1])

        self.assertEqual(q.subtotal, qp1.get_subtotal + qp2.get_subtotal)

    def test_tax_amount(self):
        c = quick_create_client()[0]
        q = quick_create_quotation(c)[0]
        p = quick_create_product(2)
        qp1 = quick_create_quotationProduct(q, p[0])
        qp2 = quick_create_quotationProduct(q, p[1])

        self.assertEqual(q.tax_amount, (qp1.get_subtotal + qp2.get_subtotal) * 0.05)

    def test_total_with_tax(self):
        c = quick_create_client()[0]
        q = quick_create_quotation(c)[0]
        p = quick_create_product(2)
        qp1 = quick_create_quotationProduct(q, p[0])
        qp2 = quick_create_quotationProduct(q, p[1])
        
        self.assertEqual(q.total_with_tax, (qp1.get_subtotal + qp2.get_subtotal) * 1.05)

class QuotationProductTest(TestCase):
    def test_create_quotationProduct(self):
        c = quick_create_client()[0]
        q = quick_create_quotation(c)[0]
        p = quick_create_product()[0]
        qp = QuotationProduct.objects.create(
            quotation = q,
            product = p,
            quantity = 1
        )
        
        self.assertEqual(qp.get_subtotal, qp.quantity*p.product_price)
