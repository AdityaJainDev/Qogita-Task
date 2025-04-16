import csv
from django.core.management.base import BaseCommand
from stocklist.models import Product

class Command(BaseCommand):
    help = 'Import products from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        with open(options['csv_file'], 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                product = Product(
                    title=row['Product Title'].strip(),
                    price=float(row['Variant Price']),
                    sku=row['Variant Sku'].strip(),
                    barcode=row['Variant Barcode'].strip(),
                    inventory_quantity=int(row['Variant Inventory Quantity']),
                    size=int(row['Product.custom.pack_size'])
                )
                try:
                    product.save()
                    self.stdout.write(self.style.SUCCESS(f'Successfully imported {product.title}'))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'Failed to import {row["Product Title"]}: {str(e)}'))