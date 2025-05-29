from django.db import models

class Voucher(models.Model):
    nome = models.CharField("Nome do Voucher", max_length=100)

    def __str__(self):
        return self.nome


class Agendamento(models.Model):
    nome = models.CharField("Nome", max_length=100, null=True, blank=True)
    nome_completo = models.CharField("Nome completo", max_length=200, null=True, blank=True)
    email = models.EmailField("Email",null=True, blank=True)
    seu_email = models.EmailField("Seu Email", null=True, blank=True)
    data = models.DateField("Selecione uma data", null=True, blank=True)
    voucher = models.ForeignKey(Voucher, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Selecione seu Voucher")
    telefone = models.CharField("Telefone", max_length=20, null=True, blank=True)
    phone = models.CharField("Phone", max_length=20, null=True, blank=True)
    observacao = models.TextField("Observação", null=True, blank=True)

    def __str__(self):
        return f"{self.nome_completo} - {self.voucher}"
