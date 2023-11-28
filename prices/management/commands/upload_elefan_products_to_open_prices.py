import json
import time

from django.core.management.base import BaseCommand

from common.api import openfoodfacts


ELEFAN_OSM_ID = 1392117416
ELEFAN_OSM_TYPE = "NODE"
ELEFAN_PRODUCTS_FILE = "local_data/20231127_elefan_products.json"
FAMILLE_TO_EXCLUDE_MIN = 93
FAMILLE_TO_EXCLUDE_EXTRA = [43, 44, 73]
PRICE_DATE = "2023-11-27"


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
            p
            for p in elefan_products_with_ean_13
            if ((p["famille"]["id"] < FAMILLE_TO_EXCLUDE_MIN) and (p["famille"]["id"] not in FAMILLE_TO_EXCLUDE_EXTRA))
        ]
        print("Nombre d'articles uploadables avec EAN 13:", len(elefan_products_with_ean_13_filtered))

        progress = 0
        for index, elefan_price in enumerate(elefan_products_with_ean_13_filtered[100:]):
            print("=================")
            try:
                PRICE = {
                    "product_code": str(elefan_price["code"]),
                    "price": elefan_price["prix_vente"],
                    "currency": "EUR",
                    "location_osm_id": ELEFAN_OSM_ID,
                    "location_osm_type": ELEFAN_OSM_TYPE,
                    "date": PRICE_DATE,
                }
                print(PRICE)
                response = openfoodfacts.create_price(price=PRICE)
                print(response.status_code)
                print(response.content)
                time.sleep(1)
                progress += 1
                if (progress % 50) == 0:
                    print(f"{progress}...")
                    time.sleep(10)
            except Exception as e:
                print("Error for price index", index)
                print(e)
