import pytest
from decimal import Decimal
from quotations.tests.factories import (
    ProductFactory,
    OrderProductFactory
)

pytestmark = pytest.mark.django_db

def test_get_subtotal_with_quotation_and_products():
    p = ProductFactory(price=100)
    op = OrderProductFactory(product=p, quantity=2)
    assert op.get_subtotal == Decimal('200')