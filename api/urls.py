from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework import routers

from api.prices.views import PriceViewSet
from api.products.views import ProductViewSet


app_name = "api"

router = routers.DefaultRouter()
router.register(r"prices", PriceViewSet, basename="prices")
router.register(r"products", ProductViewSet, basename="products")

urlpatterns = [
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularSwaggerView.as_view(url_name="api:schema"), name="swagger-ui"),
    path("redoc/", SpectacularRedocView.as_view(url_name="api:schema"), name="redoc"),
]

urlpatterns += router.urls
