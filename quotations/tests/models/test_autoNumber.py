import pytest
from django.utils import timezone
from freezegun import freeze_time
from quotations.tests.factories import QuotationFactory

pytestmark = pytest.mark.django_db

def test_first_number_is_001():
    q = QuotationFactory()
    year = timezone.now().year
    assert q.number == f"Q-{year}-001"

def test_number_increment():
    q1 = QuotationFactory()
    q2 = QuotationFactory()

    num1 = int(q1.number.split('-')[-1])
    num2 = int(q2.number.split('-')[-1])
    assert num2 == (num1 + 1)

@freeze_time("2025-12-31")
def test_cross_year_reset_2025():
    q = QuotationFactory()
    assert q.number == "Q-2025-001"


@freeze_time("2026-01-01")
def test_cross_year_reset_2026():
    q = QuotationFactory()
    assert q.number == "Q-2026-001"