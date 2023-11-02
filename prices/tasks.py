from common.api import openstreetmap
from prices.models import Price


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
