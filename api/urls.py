from rest_framework import routers

from api.prices.views import PriceViewSet


app_name = "api"

router = routers.DefaultRouter()
router.register(r"prices", PriceViewSet, basename="prices")

urlpatterns = []

urlpatterns += router.urls
