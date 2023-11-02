from rest_framework import mixins, viewsets

from api.products.serializers import ProductSerializer
from products.models import Product


class ProductViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
