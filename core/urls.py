from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('detalhes/<int:id>/', ResultadoDetailView.as_view(), name='detalhes')

]