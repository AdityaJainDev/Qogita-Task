import xml.etree.ElementTree as ET
from django.core.management.base import BaseCommand
from stocklist.models import Product
from decimal import Decimal

class Command(BaseCommand):
    help = 'Import products from XML file'

    def add_arguments(self, parser):
        parser.add_argument('xml_file', type=str, help='Path to the XML file')

    def handle(self, *args, **options):
        success = 0
        error = 0

        tree = ET.parse(options['xml_file'])
        root = tree.getroot()
        
        items = root.find('items').findall('item')

        for item in items:
            title = item.find('articleName').text.strip()

            price = item.find('priceWithoutVat').text.strip()
            price = Decimal(price) if price else Decimal('0.00')

            sku = item.find('articleId').text.strip()

            barcode = item.find('articleEAN').text
            barcode = barcode.strip() if barcode else 'N/A'

            inventory_quantity = item.find('stockQuantity').text.strip()
            inventory_quantity = int(inventory_quantity) if inventory_quantity else 0

            size = item.find('volume').text.strip()
            size = int(size) if size else 0

            product = Product(
                title=title,
                price=price,
                sku=sku,
                barcode=barcode,
                inventory_quantity=inventory_quantity,
                size=size
            )
            try:
                product.save()
                success += 1
            except Exception as e:
                print("There was an error", e)
                error += 1

        print(f"Import completed. Successfully imported {success} products. Failed to import {error} products.")