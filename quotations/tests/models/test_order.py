import pytest
from decimal import Decimal
from quotations.tests.factories import (
    OrderFactory, 
    ProductFactory,
    OrderProductFactory
)

pytestmark = pytest.mark.django_db

# -------------------------
# 基本建立測試, smoke test(測試關聯，不測試邏輯)
# -------------------------

def test_create_order_has_company_and_client():
    # smoke test(測試關聯，不測試邏輯)
    o = OrderFactory()
    assert o.company.__class__.__name__ == "Company"
    assert o.client.__class__.__name__ == "Client"

# -------------------------
# 金額計算測試
# -------------------------

def test_subtotal_with_orderproducts():
    o = OrderFactory(tax_rate=10)
    p = ProductFactory(price=200)
    OrderProductFactory(order=o, product=p, quantity=2)

    assert o.subtotal == Decimal('400')
    assert o.tax_amount == Decimal('40')
    assert o.total_with_tax == Decimal('440')