from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework import routers

from api.locations.views import LocationViewSet
from api.prices.views import PriceViewSet
from api.products.views import ProductViewSet


app_name = "api"

router = routers.DefaultRouter()
router.register(r"prices", PriceViewSet, basename="prices")
router.register(r"products", ProductViewSet, basename="products")
router.register(r"locations", LocationViewSet, basename="locations")

urlpatterns = [
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularSwaggerView.as_view(url_name="api:schema"), name="swagger-ui"),
    path("redoc/", SpectacularRedocView.as_view(url_name="api:schema"), name="redoc"),
]

urlpatterns += router.urls
