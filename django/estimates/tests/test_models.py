from django.test import TestCase
from django.utils import timezone
from estimates.models import Client, Product, Quotation, QuotationProduct, Order, OrderProduct, SubProduct
from datetime import date
from decimal import Decimal

def quick_create_client(num=1):
    """ Inter a number 'num' to generate multiple Clients."""
    for i in range(num):
        c = Client.objects.create(
            name = f'測試客戶{i}',
            phone = f'0912345{i}',
            gui = f'{i}'
        )
def quick_create_product(num=1):
    """ Inter a number 'num' to generate multiple Products."""
    for i in range(num):
        p = Product.objects.create(
            name = f'測試工作項次{i}',
            price = i * 1000
        )
def quick_create_quotation(client):
    """ Input a paramter 'Client' to generate a Quotation."""
    return Quotation.objects.create(
        client = client,
        name = '測試報價單名稱',
        address = '測試地址',
        contact_name = '測試聯絡人',
        area = 199.005,
        tax_rate = 5,
        status = 'draft',
        note = '測試備註'
    )
def quick_create_quotation_item(q=None, p=None):
    if q == None:
        quick_create_client()
        c = Client.objects.all().first()
        quick_create_quotation(c)
        q = Quotation.objects.all().first()
    if p == None:
        quick_create_product()
        p = Product.objects.all().first()
    qi = QuotationProduct.objects.create(
        quotation = q,
        product = p,
        quantity = 1
    )
    return qi
def quick_create_order(client):
    """ Input a paramter 'Client' to generate a Order."""
    return Order.objects.create(
        client = client,
        address = '測試地址',
        tax_rate = 5,
        note = '測試備註'
    )

class ClientTest(TestCase):
    def test_create_client(self):
        c = Client.objects.create(
            name = '測試名稱',
            phone = '02-12345678',
            gui = '12345678'
        )

        self.assertEqual(c.name, '測試名稱')
        self.assertEqual(c.phone, '02-12345678')
        self.assertEqual(c.gui, '12345678')

class ProductTest(TestCase):
    def test_create_product(self):
        p = Product.objects.create(
            name = '測試商品',
            price = 666,
            is_active = True
        )

        self.assertEqual(p.name, '測試商品')
        self.assertEqual(p.price, 666)
        self.assertEqual(p.is_active, True)

class QuotationTest(TestCase):
    def test_create_quotation(self):
        quick_create_client(1)
        c = Client.objects.all().first()
        quick_create_quotation(client=c)
        q = Quotation.objects.all().first()
        year = date.today().year
        
        self.assertEqual(q.client, c)
        self.assertEqual(q.number, f'Q-{year}-001')
        self.assertEqual(q.name, '測試報價單名稱')
        self.assertEqual(q.address, '測試地址')
        self.assertEqual(q.area, 199.005)
        self.assertEqual(q.contact_name, '測試聯絡人')
        self.assertEqual(q.created_date, date.today())
        self.assertEqual(q.tax_rate, 5)
        self.assertEqual(q.status, 'draft')
        self.assertEqual(q.get_status_display(), '草稿')
        self.assertEqual(q.note, '測試備註')

    def test_method_quotation(self):
        quick_create_client(1)
        quick_create_product(2)
        c = Client.objects.all().first()
        quick_create_quotation(client=c)
        q = Quotation.objects.all().first()
        ps = Product.objects.all()
        feature_total = 0
        for i in range(len(ps)):
            qi = QuotationProduct.objects.create(
                quotation = q,
                product = ps[i],
                quantity = 1
            )
            feature_total += qi.get_subtotal

        self.assertEqual(q.subtotal, feature_total)
        self.assertEqual(q.tax_amount, feature_total * q.tax_rate/(Decimal('100.00')))
        self.assertEqual(q.total_with_tax, q.subtotal + q.tax_amount)

    def test_method_quotation_convert_to_order(self):
        quick_create_client(1)
        quick_create_product(1)
        c = Client.objects.all().first()
        p = Product.objects.all().first()
        quick_create_quotation(c)
        q = Quotation.objects.all().first()
        for i in range(3):
            qi = QuotationProduct.objects.create(
                quotation = q,
                product = p,
                quantity = i
            )
        o = q.convert_to_order()
        year = date.today().year

        self.assertEqual(o.client, q.client)
        for i in range(len(o.products.all())):
            self.assertEqual(o.products.all()[i], q.products.all()[i])
        self.assertEqual(o.name, q.name)
        self.assertEqual(o.number, f'Order-{year}-001')
        self.assertEqual(o.address, q.address)
        self.assertEqual(o.contact_name, q.contact_name)
        self.assertEqual(o.area, q.area)
        self.assertEqual(o.created_date, date.today())
        self.assertEqual(o.tax_rate, 5)
        self.assertEqual(o.get_status_display(), '未處理')
        self.assertEqual(o.note, q.note)
        self.assertEqual(o.subtotal, q.subtotal)
        self.assertEqual(o.tax_amount, o.tax_amount)
        self.assertEqual(o.total_with_tax, q.total_with_tax)

    def test_number_continues_after_deletion(self):
        year = timezone.now().year
        quick_create_client()
        c = Client.objects.all().first()
        q1 = quick_create_quotation(c)
        q2 = quick_create_quotation(c)
        q3 = quick_create_quotation(c)

        self.assertEqual(q1.number, f'Q-{year}-001')
        self.assertEqual(q2.number, f'Q-{year}-002')
        self.assertEqual(q3.number, f'Q-{year}-003')

        q2.delete()

        q4 = quick_create_quotation(c)
        self.assertEqual(q4.number, f'Q-{year}-004')

class QuotationProductTest(TestCase):
    def test_create_QuotationProduct(self):
        quick_create_client(1)
        quick_create_product(1)
        c = Client.objects.all().first()
        p = Product.objects.all().first()
        q = Quotation.objects.create(
            client = c,
            address = '測試地址',
            status = '草稿',
            note = '測試備註'
        )
        qi = QuotationProduct.objects.create(
            quotation = q,
            product = p,
            quantity = 1
        )

        self.assertEqual(qi.quotation, q)
        self.assertEqual(qi.product, p)
        self.assertEqual(qi.quantity, 1)
        self.assertEqual(qi.get_subtotal, p.price * qi.quantity)

class OrderTest(TestCase):
    def test_create_order(self):
        quick_create_client()
        quick_create_product()
        c = Client.objects.all().first()
        o = Order.objects.create(
            client = c,
            address = '測試地址',
            note = '測試備註'
        )
        year = date.today().year

        self.assertEqual(o.client, c)
        self.assertEqual(o.number, f'Order-{year}-001')
        self.assertEqual(o.address, '測試地址')
        self.assertEqual(o.created_date, date.today())
        self.assertEqual(o.tax_rate, 5)
        self.assertEqual(o.get_status_display(), '未處理')
        self.assertEqual(o.note, '測試備註')
    
    def test_method_order(self):
        quick_create_client(1)
        quick_create_product(2)
        c = Client.objects.all().first()
        o = Order.objects.create(
            client = c,
            address = '測試地址',
            tax_rate = 5,
            note = '測試備註'
        )
        ps = Product.objects.all()
        feature_total = 0
        for i in range(len(ps)):
            oi = OrderProduct.objects.create(
                order = o,
                product = ps[i],
                quantity = 1
            )
            feature_total += oi.get_subtotal

        self.assertEqual(o.subtotal, feature_total)
        self.assertEqual(o.tax_amount, feature_total * o.tax_rate/(Decimal('100.00')))
        self.assertEqual(o.total_with_tax, o.subtotal + o.tax_amount)

    def test_number_continues_after_deletion(self):
        """Test"""
        year = timezone.now().year
        quick_create_client()
        c = Client.objects.all().first()
        o1 = quick_create_order(c)
        o2 = quick_create_order(c)
        o3 = quick_create_order(c)

        self.assertEqual(o1.number, f'Order-{year}-001')
        self.assertEqual(o2.number, f'Order-{year}-002')
        self.assertEqual(o3.number, f'Order-{year}-003')

        o2.delete()

        o4 = quick_create_order(c)
        self.assertEqual(o4.number, f'Order-{year}-004')
        
class OrderProductTest(TestCase):
    def test_create_OrderProduct(self):
        quick_create_client(1)
        quick_create_product(1)
        c = Client.objects.all().first()
        p = Product.objects.all().first()
        o = Order.objects.create(
            client = c,
            address = '測試地址'
        )
        oi = OrderProduct.objects.create(
            order = o,
            product = p,
            quantity = 1
        )

        self.assertEqual(oi.order, o)
        self.assertEqual(oi.product, p)
        self.assertEqual(oi.quantity, 1)

    def test_method_OrderProduct(self):
        quick_create_client(1)
        quick_create_product(2)
        c = Client.objects.all().first()
        ps = Product.objects.all()
        o = Order.objects.create(
            client = c,
            address = '測試地址'
        )
        for i in range(len(ps)):
            oi = OrderProduct.objects.create(
                order = o,
                product = ps[i],
                quantity = i
            )
            self.assertEqual(oi.get_subtotal, oi.quantity * ps[i].price)

class SubProductTest(TestCase):
    def test_create_subproduct(self):
        quick_create_product()
        p = Product.objects.all().first()
        subp = SubProduct.objects.create(
            product = p,
            name = '測試子項目')
        self.assertTrue(SubProduct.objects.all().count(), 1)
        self.assertEqual(subp.name, '測試子項目')
        self.assertEqual(subp.product, p)