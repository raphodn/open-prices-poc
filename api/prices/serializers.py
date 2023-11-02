from rest_framework import serializers

from api.products.serializers import ProductSerializer
from prices.models import Price


class PriceSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    location_osm_name = serializers.CharField(read_only=True)
    created = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Price
        fields = Price.SERIALIZED_FIELDS
        read_only_fields = Price.READONLY_FIELDS
