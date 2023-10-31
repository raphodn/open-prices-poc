from rest_framework import mixins, viewsets

from api.prices.serializers import PriceSerializer
from prices.models import Price


class PriceViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, args, kwargs)
