import xml.etree.ElementTree as ET
from django.core.management.base import BaseCommand
from stocklist.models import Product

class Command(BaseCommand):
    help = 'Import products from XML file'

    def add_arguments(self, parser):
        parser.add_argument('xml_file', type=str, help='Path to the XML file')

    def handle(self, *args, **options):
        tree = ET.parse(options['xml_file'])
        root = tree.getroot()
        for product in root.findall('product'):
            title = product.find('title').text
            price = product.find('variants').find('price').text
            sku = product.find('variants').find('sku').text
            barcode = product.find('variants').find('barcode').text
            inventory_quantity = product.find('variants').find('inventory_quantity').text
            pack_size = product.find('custom_fields').find('pack_size').text
            product = Product(
                title=title,
                price=price,
                sku=sku,
                barcode=barcode,
                inventory_quantity=inventory_quantity,
                pack_size=pack_size
            )
            try:
                product.save()
                self.stdout.write(self.style.SUCCESS(f'Successfully imported {title}'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Failed to import {title}: {str(e)}'))