from django.shortcuts import render

from django.views.generic.base import TemplateView

class MainPageView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'Mikl'
        return context

def about(request):
    return render(request, 'about.html')