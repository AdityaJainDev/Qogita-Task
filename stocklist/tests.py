from django.test import TestCase
from rest_framework.test import APITestCase
from .models import Product
from decimal import Decimal

class ProductAPITests(APITestCase):
    def setUp(self):
        self.product = Product.objects.create(
            title="Test Product",
            price=Decimal("9.99"),
            sku="TEST-SKU-001",
            barcode="123456789",
            inventory_quantity=10,
            size=6
        )

    def test_list_products(self):
        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 1)

    def test_delete_product(self):
        response = self.client.delete(f'/api/products/{self.product.id}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Product.objects.count(), 0)

class ImportCommandTests(TestCase):
    def test_import_csv(self):
        from django.core.management import call_command
        call_command('import_stock_csv', 'sample_cosmetics_stocklist.csv')
        self.assertTrue(Product.objects.exists())

    def test_import_xml(self):
        from django.core.management import call_command
        call_command('import_stock_xml', 'wholesale-feed.xml')
        self.assertTrue(Product.objects.exists())