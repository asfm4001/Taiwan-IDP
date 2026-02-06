from django.test import TestCase
from quotations.models import Client

def quick_create_client(num=1):
    """ Inter a number 'num' to generate multiple Clients."""
    for i in range(num):
        c = Client.objects.create(
            name = f'測試客戶{i}',
            phone = f'0912345{i}',
            gui = f'{i}'
        )

class ClientModelTest(TestCase):
    def test_create_client(self):
        quick_create_client()
        c = Client.objects.all()[0]

        self.assertEqual(c.name, '測試客戶0')
        self.assertEqual(c.phone, '09123450')
        self.assertEqual(c.gui, '0')