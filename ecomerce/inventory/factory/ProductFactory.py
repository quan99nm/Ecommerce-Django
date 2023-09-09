import factory
from ecomerce.inventory.models import Product


class ProductFactory(factory.Factory):
    class Meta:
        model = Product

    name = factory.Faker("word")  # Example: Generate random words
    price = factory.Faker("pyfloat", positive=True, min_value=0)
    description = factory.Faker("word")
