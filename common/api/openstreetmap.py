"""
OSM types: node, way, relation
OSMPythonTools element methods: tags(), tag(key), lat(), lon(), geometry(), centerLat(), centerLon()
"""
from OSMPythonTools.api import Api
from OSMPythonTools.nominatim import Nominatim
from OSMPythonTools.overpass import Overpass


OSM_NOMINATIM_API_ENDPOINT = "https://nominatim.openstreetmap.org"


def get_nominatim_client():
    return Nominatim()


def get_api_client():
    return Api()


def get_overpass_client():
    return Overpass()


def search_location(search_query):
    client = get_nominatim_client()
    return client.query(search_query).toJSON()


def get_location_details(osm_id, osm_type="node"):
    client = Api()
    search_query = f"{osm_type}/{osm_id}"
    return client.query(search_query)


def get_location_details_with_nominatim(osm_id, osm_type="node"):
    client = get_nominatim_client()
    search_query = f"{osm_type}/{osm_id}"
    return client.query(search_query, lookup=True).toJSON()


def get_location_details_with_overpass(osm_id, osm_type="node"):
    client = get_overpass_client()
    search_query = f"{osm_type}(id:{osm_id});out;"
    return client.query(search_query).elements()
