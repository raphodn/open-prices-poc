from rest_framework import serializers

from locations.models import Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = [field.name for field in Location._meta.fields]
