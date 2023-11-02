from common.api import openfoodfacts
from products.models import Product


def fetch_product_info_from_openfoodfacts(product: Product):
    try:
        response = openfoodfacts.get_product(product.code)
        print("Product task OFF info: updating data from OpenFoodFacts")
        product.in_off = True
        product.off_db = Product.OFF_SOURCE_OFF
        if "product_name" in response["product"]:
            product.off_name = response["product"]["product_name"]
        if "image_url" in response["product"]:
            product.off_image_url = response["product"]["image_url"]
        product.save()
    except Exception as e:
        print("Product task OFF info: error returned from OpenFoodFacts")
        if e.response and e.response.status_code == 404:
            product.in_off = False
            product.save()
