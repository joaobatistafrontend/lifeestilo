from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, DetailView, View
from .models import *
from .forms import *

class IndexView(TemplateView):
    template_name = 'index.html'
    def get(self, request):
        promocoes = Promocao.objects.filter(disponivel=True)
        resultados = Resultados.objects.all()
        form = AgendamentoForm()
        return render(request, self.template_name, {'promocoes':promocoes, 'resultados':resultados, 'form':form
        })
    
    def post(self, request):
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        return self.get(request)
  


class ResultadoDetailView(DetailView):
    template_name = 'detail.html'
    def get(self, request, id):
        resultado = get_object_or_404(Resultados, id=id)
        recentes = Resultados.objects.exclude(id=resultado.id).order_by('-data_da_publicacao')[:3]
        return render(request, self.template_name, {'resultado': resultado, 'recentes':recentes})