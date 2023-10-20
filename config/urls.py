from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("prices/", include("www.prices.urls")),
    path("", include("www.pages.urls"))
]
