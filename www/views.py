from django.views.generic import DetailView, FormView, ListView, TemplateView, View


class HomeView(TemplateView):
    template_name = "www/home.html"
