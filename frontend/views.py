# Create your views here.
from django.views.generic import TemplateView

from core.models import Cultivos, Area


class IndexView(TemplateView):
    model = Cultivos
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['title'] = 'Cultivos'
        context['listCultivos'] = Cultivos.objects.all()
        context['listAreas'] = Area.objects.all()
        return context

