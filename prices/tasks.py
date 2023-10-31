from common.api import openfoodfacts
from prices.models import Price


def fetch_and_update_product_info_from_openfoodfacts(price: Price):
    # we need at least the 'product_code'
    if not price.product_code:
        print("Price task error: price without product_code")
        return

    # 'product_off_name' already filled
    if price.product_off_name:
        print("Price task info: price already has product_off_name")
        return

    # check if we already fetched data on another price
    existing_product_qs = (
        Price.objects.filter(product_code=price.product_code)
        .exclude(product_off_name__isnull=True)
        .exclude(product_off_name__exact="")
    )
    if existing_product_qs.count():
        existing_product = existing_product_qs.first()
        if existing_product.product_off_name:
            print("Price task info: found existing_product")
            price.product_in_off = existing_product.product_in_off
            price.product_off_db = existing_product.product_off_db
            price.product_off_name = existing_product.product_off_name
            price.product_off_image_url = existing_product.product_off_image_url
            price.save()
            return

    # fetch data from OFF
    try:
        response = openfoodfacts.get_product(price.product_code)
        print("Price task info: updating data from OpenFoodFacts")
        price.product_in_off = True
        price.product_off_db = Price.OFF_SOURCE_OFF
        if "product_name" in response["product"]:
            price.product_off_name = response["product"]["product_name"]
        if "image_url" in response["product"]:
            price.product_off_image_url = response["product"]["image_url"]
        price.save()
    except Exception as e:
        print("Price task info: error returned from OpenFoodFacts")
        if e.response and e.response.status_code == 404:
            price.product_in_off = False
            price.save()
