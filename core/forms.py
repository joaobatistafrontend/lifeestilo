# forms.py
from django import forms
from .models import Agendamento

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['nome_completo', 'email', 'data', 'voucher', 'telefone', 'observacao']
        widgets = {
            'nome_completo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome completo'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Seu email'}),
            'data': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'voucher': forms.Select(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefone'}),
            'observacao': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Observação'}),
        }
