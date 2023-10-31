from rest_framework import mixins, viewsets

from api.prices.filters import PriceFilter
from api.prices.serializers import PriceSerializer
from prices.models import Price


class PriceViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer
    filterset_class = PriceFilter
