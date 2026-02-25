import factory
from quotations.models import Product

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = '測試工作項目'
    price = 100
    is_active = True