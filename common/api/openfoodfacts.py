import os

from openfoodfacts import API, APIVersion, Country, Environment, Flavor


"""
Python API: https://github.com/openfoodfacts/openfoodfacts-python
Documentation: https://openfoodfacts.github.io/openfoodfacts-python/
"""


def get_client():
    return API(
        username=os.environ.get("OPENFOODFACTS_USERNAME"),
        password=os.environ.get("OPENFOODFACTS_PASSWORD"),
        country=Country.world,
        flavor=Flavor.off,
        version=APIVersion.v2,
        environment=Environment.org,
    )


def get_product(code):
    client = get_client()
    return client.product.get(code)
