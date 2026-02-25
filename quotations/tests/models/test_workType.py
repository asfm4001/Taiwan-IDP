import pytest
from quotations.tests.factories import (
    WorkTypeFactory,
    ProductFactory,
    WorkTypeProductFactory,
    SubProductFactory
)

pytestmark = pytest.mark.django_db

def test_clone_from_template_cloumn_is_correct():
    w = WorkTypeFactory()

    new_q = w.clone_from_template()

    assert new_q.__class__.__name__ == "Quotation"

    assert new_q.company == w.company
    assert new_q.client == w.client
    assert new_q.name == w.name
    assert new_q.note == w.note

def test_clone_from_template_product_is_correct():
    p1 = ProductFactory(price=100)
    p2 = ProductFactory(price=200)

    SubProductFactory(product=p1)
    SubProductFactory(product=p1)
    SubProductFactory(product=p2)

    w = WorkTypeFactory()

    WorkTypeProductFactory(worktype=w, product=p1, quantity=1)
    WorkTypeProductFactory(worktype=w, product=p2, quantity=2)


    new_q = w.clone_from_template()

    temp_products = list(w.products.all().order_by('id'))
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