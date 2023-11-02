from rest_framework import mixins, viewsets

from api.locations.serializers import LocationSerializer
from locations.models import Location


class LocationViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
