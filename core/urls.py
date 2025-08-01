from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('detalhes/<int:id>/', ResultadoDetailView.as_view(), name='detalhes')

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)