from django.views.generic import TemplateView

from prices.models import Price


class HomeView(TemplateView):
    template_name = "www/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["price_count"] = Price.objects.count()
        return context
