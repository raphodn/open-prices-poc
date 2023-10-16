from OSMPythonTools.nominatim import Nominatim


OSM_NOMINATIM_API_ENDPOINT = "https://nominatim.openstreetmap.org"


def get_client():
    return Nominatim()

def search_location(search_query):
    client = get_client()
    return client.query(search_query).toJSON()
