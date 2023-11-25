import json
import time

from django.core.management.base import BaseCommand

from common.api import openfoodfacts


ELEFAN_PRODUCTS_FILE = "local_data/20231123_elefan_products.json"
FAMILLE_TO_EXCLUDE_MIN = 93


class Command(BaseCommand):
    """
    Usage: python manage.py upload_elefan_products_to_open_prices
    """

    def handle(self, **options):
        # read json file
        f = open(ELEFAN_PRODUCTS_FILE)
        elefan_products = json.load(f)
        print("Nombre d'articles", len(elefan_products))

        # filter on products
        # - with ean13
        # - food products
        elefan_products_with_ean_13 = [p for p in elefan_products if (len(str(p["code"])) == 13)]
        print("Nombre d'articles avec EAN 13:", len(elefan_products_with_ean_13))
        elefan_products_with_ean_13_filtered = [
            p for p in elefan_products_with_ean_13 if (p["famille"]["id"] < FAMILLE_TO_EXCLUDE_MIN)
        ]
        print("Nombre d'articles uploadables avec EAN 13:", len(elefan_products_with_ean_13_filtered))

        progress = 0
        for index, elefan_price in enumerate(elefan_products_with_ean_13_filtered[1:20]):
            print("=================")
            try:
                PRICE = {
                    "product_code": str(elefan_price["code"]),
                    "price": str(elefan_price["prix_vente"]),
                    "currency": "EUR",
                    "location_osm_id": 1392117416,
                    "location_osm_type": "NODE",
                    "date": "2023-11-23",
                }
                print(PRICE)
                response = openfoodfacts.create_price(price=PRICE)
                print(response.status_code)
                print(response.content)
                time.sleep(1)
                progress += 1
                if (progress % 10) == 0:
                    print(f"{progress}...")
            except Exception as e:
                print("Error for price index", index)
                print(e)
