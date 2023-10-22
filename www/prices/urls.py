from django.urls import path

from www.prices.views import PriceCreateView, PriceListView


app_name = "prices"

urlpatterns = [
    path("", PriceListView.as_view(), name="list"),
    path("create/", PriceCreateView.as_view(), name="create"),
]
