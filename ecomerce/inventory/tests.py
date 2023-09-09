from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from ecomerce.inventory.factory.ProductFactory import ProductFactory
from .models import Product


class ProductTestCase(TestCase):
    def test_product_creation(self):
        product = ProductFactory()
        self.assertIsInstance(product, Product)
