import django_filters

from prices.models import Price


class PriceFilter(django_filters.FilterSet):
    price__gt = django_filters.NumberFilter(field_name="price", lookup_expr="gt")
    price__gte = django_filters.NumberFilter(field_name="price", lookup_expr="gte")
    price__lt = django_filters.NumberFilter(field_name="price", lookup_expr="lt")
    price__lte = django_filters.NumberFilter(field_name="price", lookup_expr="lte")

    class Meta:
        model = Price
        fields = ["product_code", "price", "location_osm_id", "date"]
