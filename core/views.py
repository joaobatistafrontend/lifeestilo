from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, View
from .models import *

class IndexView(TemplateView):
    template_name = 'index.html'
    def get(self, request):
        promocoes = Promocao.objects.filter(disponivel=True)
        resultados = Resultados.objects.all()
        return render(request, self.template_name, {'promocoes':promocoes, 'resultados':resultados})
    

class DetailView(View):
    template_name = 'detail.html'
    def get(self, request):
        return render(request, self.template_name)
    