from rest_framework import mixins, viewsets

from api.prices.filters import PriceFilter
from api.prices.serializers import PriceSerializer
from prices.models import Price


class PriceViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Price.objects.select_related("product", "location").all()
    serializer_class = PriceSerializer
    filterset_class = PriceFilter

    def perform_create(self, serializer):
        serializer.save(source=Price.SOURCE_API)
