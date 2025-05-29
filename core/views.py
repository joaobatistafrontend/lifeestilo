from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, View

class IndexView(TemplateView):
    template_name = 'index.html'
    def get(self, request):
        return render(request, self.template_name)
    

class DetailView(View):
    template_name = 'detail.html'
    def get(self, request):
        return render(request, self.template_name)
    