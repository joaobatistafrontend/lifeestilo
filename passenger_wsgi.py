import os
import sys

# Adiciona o caminho do projeto ao sys.path
sys.path.insert(0, os.path.dirname(__file__))

# Define as configurações do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'life.settings')

# Instância do WSGI para o Phusion Passenger do cPanel
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
