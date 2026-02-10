import datetime
from unittest.mock import patch
from django.utils import timezone
from django.test import TestCase
from quotations.tests.factories import QuotationFactory

class AutoNumberMixTest(TestCase):
    def test_first_number_is_001(self):
        q = QuotationFactory()
        year = timezone.now().year
        self.assertEqual(q.number, f"Q-{year}-001")
    def test_number_increment(self):
        q1 = QuotationFactory()
        q2 = QuotationFactory()

        num1 = int(q1.number.split('-')[-1])
        num2 = int(q2.number.split('-')[-1])
        self.assertEqual(num2, num1 + 1)
    
    @patch('django.utils.timezone.now')
    def test_cross_year_reset(self, mock_now):
        # 模擬 2025
        mock_now.return_value = timezone.datetime(2025, 12, 31, tzinfo=datetime.timezone.utc)
        q1 = QuotationFactory()
        self.assertEqual(q1.number, 'Q-2025-001')

        # 模擬 2026
        mock_now.return_value = timezone.datetime(2026, 1, 1, tzinfo=datetime.timezone.utc)
        q2 = QuotationFactory()
        self.assertEqual(q2.number, 'Q-2026-001')