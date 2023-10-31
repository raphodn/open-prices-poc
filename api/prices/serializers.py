from rest_framework import serializers

from prices.models import Price


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ["product_code", "price", "currency", "location_osm_id", "location_name", "date", "created"]
