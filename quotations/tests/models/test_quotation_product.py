import pytest
from quotations.tests.factories import (
    ProductFactory,
    QuotationProductFactory
)

pytestmark = pytest.mark.django_db

def test_get_subtotal_with_quotation_and_products():
    p = ProductFactory(price=100)
    qp = QuotationProductFactory(product=p, quantity=2)
    assert qp.get_subtotal == 200
