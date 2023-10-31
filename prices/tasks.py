from common.api import openfoodfacts
from prices.models import Price


def fetch_and_update_product_info(price: Price):
    # we need at least the 'product_code'
    if not price.product_code:
        return

    # 'product_off_name' already filled
    if price.product_off_name:
        return

    # check if we already fetched data on another price
    existing_product_qs = (
        Price.objects.filter(product_code=price.product_code)
        .exclude(product_off_name__isnull=True)
        .exclude(product_off_name__exact="")
    )
    if existing_product_qs.count():
        existing_product = existing_product_qs.first()
        price.product_in_off = existing_product.product_in_off
        price.product_off_db = existing_product.product_off_db
        price.product_off_name = existing_product.product_off_name
        price.product_off_image_url = existing_product.product_off_image_url
        price.save()

    try:
        response = openfoodfacts.get_product(price.product_code)
        if len(response["errors"]):
            price.product_in_off = False
        else:
            price.product_in_off = True
            price.product_off_db = Price.OFF_SOURCE_OFF
            price.product_off_name = response["product"]["product_name"]
            price.product_off_image_url = response["product"]["image_url"]
            price.save()
    except:  # noqa
        return
