# Create your views here.
from django.views.generic import TemplateView
import matplotlib.pyplot as plt
from io import StringIO
import numpy as np

from core.models import Cultivos, Area


class IndexView(TemplateView):
    model = Cultivos
    template_name = 'index.html'

    def return_graph(self):
        x = np.arange(0, np.pi * 3, .1)
        y = np.sin(x)

        fig = plt.figure()
        plt.plot(x, y)

        imgdata = StringIO()
        fig.savefig(imgdata, format='svg')
        imgdata.seek(0)

        data = imgdata.getvalue()
        return data

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['title'] = 'Cultivos'
        context['listCultivos'] = Cultivos.objects.all()
        context['listAreas'] = Area.objects.all()
        context['graph'] = self.return_graph()
        return context
