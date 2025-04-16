import csv
from django.core.management.base import BaseCommand
from stocklist.models import Product
from decimal import Decimal

class Command(BaseCommand):
    help = 'Import products from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        success = 0
        error = 0
        with open(options['csv_file'], 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                title=row['Product Title'].strip()

                price=row['Variant Price'].strip()
                price=Decimal(price) if price else Decimal('0.00')

                sku=row['Variant Sku'].strip()

                barcode=row['Variant Barcode'].strip() or 'N/A'

                inventory_quantity=row['Variant Inventory Quantity'].strip()
                inventory_quantity=int(inventory_quantity) if inventory_quantity else 0

                size=row['Product.custom.pack_size']
                size=int(size) if size else 0

                product = Product(
                    title=title,
                    price=price,
                    sku=sku,
                    barcode=barcode if barcode else 'N/A',
                    inventory_quantity=inventory_quantity if inventory_quantity else 0,
                    size=size if size else 0
                )
                try:
                    product.save()
                    success += 1
                except Exception as e:
                    print("There was an error", e)
                    error += 1
                    
        print(f"Import completed. Successfully imported {success} products. Failed to import {error} products.")