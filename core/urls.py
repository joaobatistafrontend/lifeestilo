from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('detalhes/', DetailView.as_view(), name='detalhes'),
]