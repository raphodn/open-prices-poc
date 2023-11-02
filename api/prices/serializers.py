from rest_framework import serializers

from prices.models import Price


class PriceSerializer(serializers.ModelSerializer):
    location_osm_name = serializers.CharField(read_only=True)
    created = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Price
        fields = Price.SERIALIZED_FIELDS
