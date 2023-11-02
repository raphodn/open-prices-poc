from common.api import openfoodfacts, openstreetmap
from prices.models import Price


def fetch_and_update_product_info_from_openfoodfacts(price: Price):
    # we need at least the 'product_code'
    if not price.product_code:
        print("Price task OFF error: price without product_code")
        return

    # 'product_off_name' already filled
    if price.product_off_name:
        print("Price task OFF info: price already has product_off_name")
        return

    # check if we already fetched data on another price
    existing_product_qs = (
        Price.objects.filter(product_code=price.product_code)
        .exclude(product_off_name__isnull=True)
        .exclude(product_off_name__exact="")
    )
    if existing_product_qs.count():
        existing_product = existing_product_qs.first()
        print("Price task OFF info: found existing product with same product_code")
        price.product_in_off = existing_product.product_in_off
        price.product_off_db = existing_product.product_off_db
        price.product_off_name = existing_product.product_off_name
        price.product_off_image_url = existing_product.product_off_image_url
        price.save()
        return

    # fetch data from OFF
    try:
        response = openfoodfacts.get_product(price.product_code)
        print("Price task OFF info: updating data from OpenFoodFacts")
        price.product_in_off = True
        price.product_off_db = Price.OFF_SOURCE_OFF
        if "product_name" in response["product"]:
            price.product_off_name = response["product"]["product_name"]
        if "image_url" in response["product"]:
            price.product_off_image_url = response["product"]["image_url"]
        price.save()
    except Exception as e:
        print("Price task OFF info: error returned from OpenFoodFacts")
        if e.response and e.response.status_code == 404:
            price.product_in_off = False
            price.save()


def fetch_and_update_location_info_from_openstreetmap(price: Price):
    # we need at least the 'location_osm_id'
    if not price.location_osm_id:
        print("Price task OSM error: price without location_osm_id")
        return

    # # 'location_osm_name' already filled
    # if price.location_osm_name:
    #     print("Price task OSM info: price already has location_osm_name")
    #     return

    # check if we already fetched data on another price
    existing_product_qs = (
        Price.objects.filter(location_osm_id=price.location_osm_id)
        .exclude(location_osm_type__isnull=True)
        .exclude(location_osm_type__exact="")
    )
    if existing_product_qs.count():
        existing_product = existing_product_qs.first()
        print("Price task OSM info: found existing product with same location_osm_id")
        price.location_osm_type = existing_product.location_osm_type
        price.location_osm_name = existing_product.location_osm_name
        price.location_osm_lat = existing_product.location_osm_lat
        price.location_osm_lon = existing_product.location_osm_lon
        price.save()
        return

    # fetch data from OFF
    # only works for osm_type=node
    try:
        response = openstreetmap.get_location_details_with_nominatim(price.location_osm_id, osm_type="node")
        print("Price task OSM info: updating data from OpenStreetMap")
        if len(response):
            price.location_osm_type = Price.OSM_TYPE_NODE
            if "display_name" in response[0]:
                price.location_osm_name = response[0]["display_name"]
            if "lat" in response[0]:
                price.location_osm_lat = response[0]["lat"]
            if "lon" in response[0]:
                price.location_osm_lon = response[0]["lon"]
            price.save()
    except Exception as e:
        print("Price task OSM info: error returned from OpenStreetMap")
        if e.response and e.response.status_code == 404:
            return
