import pytest
from decimal import Decimal
from quotations.tests.factories import (
    QuotationFactory, 
    ProductFactory,
    QuotationProductFactory,
    SubProductFactory
)
from quotations.models import OrderProduct

pytestmark = pytest.mark.django_db

# -------------------------
# 基本建立測試, smoke test(測試關聯，不測試邏輯)
# -------------------------

def test_quotation_has_company_and_client():
    q = QuotationFactory()
    assert q.company.__class__.__name__ == "Company"
    assert q.client.__class__.__name__ == "Client"

# -------------------------
# 金額計算測試
# -------------------------

def test_subtotal_with_quotationproducts():
    q = QuotationFactory(tax_rate=Decimal("5"))
    p = ProductFactory(price=200)
    qp = QuotationProductFactory(quotation=q, product=p, quantity=2)
    assert q.subtotal == Decimal("400")
    assert q.tax_amount == Decimal("20")
    assert q.total_with_tax == Decimal("420")

# -------------------------
# convert_to_order
# -------------------------

def test_convert_to_order_creates_order_with_same_fields():
    q = QuotationFactory()

    new_o = q.convert_to_order()

    assert new_o.pk is not None
    assert new_o.__class__.__name__ == "Order"

    # DB fields
    assert new_o.company == q.company
    assert new_o.client == q.client
    assert new_o.name == q.name
    assert new_o.address == q.address
    assert new_o.area == q.area
    assert new_o.tax_rate == q.tax_rate
    assert new_o.note == q.note

def test_convert_to_order_creates_order_products():
    q = QuotationFactory()
    p = ProductFactory()
    qp = QuotationProductFactory(quotation=q, product=p)

    o = q.convert_to_order()

    ops = OrderProduct.objects.filter(order=o)

    # 確定 轉換成訂單後僅有一筆資料
    assert ops.count() == 1

    op = ops.get()

    assert op.product == p
    assert op.quantity == qp.quantity


@pytest.mark.skip(reason="move clone_from_template from quotation to worktype")
def test_method_clone_from_template_cloumn_is_correct():
    q_temp = QuotationFactory()

    new_q = q_temp.clone_from_template()

    assert new_q.__class__.__name__ == "Quotation"

    assert new_q.company == q_temp.company
    assert new_q.client == q_temp.client
    assert new_q.name == q_temp.name
    assert new_q.address == q_temp.address
    assert new_q.area == q_temp.area
    assert new_q.tax_rate == q_temp.tax_rate
    assert new_q.status == q_temp.status
    assert new_q.note == q_temp.note


@pytest.mark.skip(reason="move clone_from_template from quotation to worktype")
def test_method_clone_from_template_products_is_correct():
    q_temp = QuotationFactory()

    p1_temp = ProductFactory(price=100)
    p2_temp = ProductFactory(price=200)

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
    assert len(temp_products) == len(new_products)

    for temp_p, new_p in zip(temp_products, new_products):
        # 檢核 product不是同一筆資料
        assert temp_p.id != new_p.id

        # column
        assert temp_p.name == new_p.name
        assert temp_p.price == new_p.price

        temp_subs = list(temp_p.subproducts.all().order_by('id'))
        new_subs = list(new_p.subproducts.all().order_by('id'))

        # 檢核subproducts數量是否相符
        assert len(temp_subs) == len(new_subs)

        for temp_sb, new_sb in zip(temp_subs, new_subs):
            # 檢核 subproduct不是同一筆資料
            assert temp_sb.id != new_sb.id

            # column
            assert temp_sb.name == new_sb.name