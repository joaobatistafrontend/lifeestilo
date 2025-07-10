from django.contrib import admin
from .models import Voucher, Doutoras, Agendamento, Promocao, Resultados

@admin.register(Voucher)
class VoucherAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']

@admin.register(Doutoras)
class DoutorasAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao_curricular']
    search_fields = ['nome', 'descricao_curricular']

@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ['nome_completo', 'email', 'telefone', 'data', 'voucher']
    search_fields = ['nome_completo', 'email']
    list_filter = ['data', 'voucher']

@admin.register(Promocao)
class PromocaoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao_curta', 'disponivel']
    list_filter = ['disponivel']
    search_fields = ['nome', 'descricao_curta']

@admin.register(Resultados)
class Resultadosdmin(admin.ModelAdmin):
    list_display = ['doutora_responsavel', 'assunto', 'data_da_publicacao', 'mostra']
    search_fields = ['assunto', 'descricao']
    list_filter = ['data_da_publicacao']
