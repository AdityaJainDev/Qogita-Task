# Qogita Task

This is a Django project that provides an API for managing a stocklist of products. The API allows you to perform operations like retreiving and deleting products.

## Setup

1. Clone the repo.
2. Create a virtual environment and activate it.
3. Install the required packages using `pip install -r requirements.txt`.
4. Run `python manage.py migrate` to create the database tables.
5. Run `python manage.py runserver` to start the development server.

## Importing Products

To import products from a CSV or XML file, use the following commands:

- `python manage.py import_stock_csv <path_to_csv_file>`
- `python manage.py import_stock_xml <path_to_xml_file>`

## API Endpoints

The API provides the following endpoints:

- `GET /api/products/`: Retrieve a list of all products.
- `GET /api/products/?search=<query>`: Search for products by title, sku, or barcode.
- `DELETE /api/products/<id>/`: Delete a product by id.

`django-filter` is used to filter products by sku, barcode, and id.

## Pagination

Pagination is provded for the API, with 20 items displayed on each page. 

## Test

To run the tests, use the following command:

`python manage.py test`
