from quotations.models import *
"""
測試時使用的套件不納入"測試本身"，僅供測試時使用
"""
def create_client(**kwargs):
    return Client.objects.create(
        name = kwargs.get('name', '測試客戶'),
        gui = kwargs.get('gui'),
        phone = kwargs.get('phone')
    )

def create_company(**kwargs):
    return Company.objects.create(
        title = kwargs.get('title', '測試公司'),
        address = kwargs.get('address'),
        phone = kwargs.get('phone'),
        fax = kwargs.get('fax'),
        tax_code = kwargs.get('tax_code'),
        icon = kwargs.get('icon'),
        stamp = kwargs.get('stamp'),
        engineer_display = kwargs.get('engineer_display', True)
    )

def create_product(**kwargs):
    return Product.objects.create(
        name = kwargs.get('name', '測試工作項目'),
        price = kwargs.get('price', 100),
        is_active = kwargs.get('is_active', True)
    )

def create_subProduct(**kwargs):
    return SubProduct.objects.create(
        product = kwargs.get('product'),
        name = kwargs.get('name')
    )

def create_quotation(
        *,
        company = None, 
        client = None,
        name = '測試施作',
        address = '測試地址',
        contact_name = '測試聯絡人',
        area = 100,
        tax_rate = Decimal('5'),
        status = 'draft',
        note = '測試備註'
        ):
    if company is None:
        company = create_company()
    if client is None:
        client = create_client()

    return Quotation.objects.create(
        company=company,
        client=client,
        name=name,
        address=address,
        contact_name=contact_name,
        area=area,
        tax_rate=tax_rate,
        status=status,
        note=note
    )

def create_order(
        *,
        client=None,
        address = '測試地址',
        tax_rate = Decimal('5'),
        note = '測試備註'
        ):
    if client is None:
        client = create_client()
    return Order.objects.create(
        client = client,
        address = address,
        tax_rate = tax_rate,
        note = note
    )

def add_product_to_quotation(quotation, product, quantity=1):
    return QuotationProduct.objects.create(
        quotation=quotation,
        product=product,
        quantity=quantity
    )