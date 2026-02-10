import factory
from quotations.models import Client

class ClientFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Client

    name = factory.Sequence(lambda n: f"測試客戶 {n}")
    gui = '1234567'
    phone = '0912345678'