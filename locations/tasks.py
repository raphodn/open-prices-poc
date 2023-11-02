from common.api import openstreetmap
from locations.models import Location


def fetch_product_info_from_openstreetmap(location: Location):
    try:
        response = openstreetmap.get_location_details_with_nominatim(location.osm_id, osm_type="node")
        print("Location task OSM info: updating data from OpenStreetMap")
        if len(response):
            location.osm_type = Location.OSM_TYPE_NODE
            if "display_name" in response[0]:
                location.osm_name = response[0]["display_name"]
            if "lat" in response[0]:
                location.osm_lat = response[0]["lat"]
            if "lon" in response[0]:
                location.osm_lon = response[0]["lon"]
            location.save()
    except Exception as e:
        print("Location task OSM info: error returned from OpenStreetMap")
        if e.response and e.response.status_code == 404:
            return
