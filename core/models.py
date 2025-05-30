from django.db import models

class Voucher(models.Model):
    nome = models.CharField("Nome do Voucher", max_length=100)
    def __str__(self):
        return self.nome
    
class Doutoras(models.Model):
    nome = models.CharField("Nome do Voucher", max_length=100)
    imagem = models.ImageField("Imagem da Promoção", upload_to='promocoes/', null=True, blank=True)
    descricao_curricular = models.CharField("escricao curricular do profissional", max_length=100, null=True, blank=True)
    def __str__(self):
        return f'{self.nome} - {self.descricao_curricular}'

class Agendamento(models.Model):
    nome = models.CharField("Nome", max_length=100, null=True, blank=True)
    nome_completo = models.CharField("Nome completo", max_length=200, null=True, blank=True)
    email = models.EmailField("Email",null=True, blank=True)
    seu_email = models.EmailField("Seu Email", null=True, blank=True)
    data = models.DateField("Selecione uma data", null=True, blank=True)
    voucher = models.ForeignKey(Voucher, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Selecione seu Voucher")
    telefone = models.CharField("Telefone", max_length=20, null=True, blank=True)
    observacao = models.TextField("Observação", null=True, blank=True)

    def __str__(self):
        return f"{self.nome_completo} - {self.voucher}"
    
DISPONIVEL_CHOICES = (
    (True, 'Sim'),
    (False, 'Não'),
)


class Promocao(models.Model):
    nome = models.CharField("Nome da Promoção", max_length=100, null=True, blank=True)
    imagem = models.ImageField("Imagem da Promoção", upload_to='promocoes/', null=True, blank=True)
    descricao_curta = models.CharField("Descrição Curta", max_length=255, null=True, blank=True)
    disponivel = models.BooleanField(choices=DISPONIVEL_CHOICES, default=True, null=True, blank=True)

    def __str__(self):
        return self.nome


class Resultados(models.Model):
    doutora_responsavel = models.ForeignKey(Doutoras, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Selecione seu Voucher")
    imagem_antes = models.ImageField("Imagem antes do processo", upload_to='antes_do_processo/', null=True, blank=True)
    imagem_depois = models.ImageField("Imagem do Resultado", upload_to='resultados/', null=True, blank=True)
    assunto = models.CharField("Assunto", max_length=100, null=True, blank=True)
    descricao = models.TextField("Descrição Detalhada", null=True, blank=True)
    data_da_publicacao = models.DateTimeField(auto_now=True, null=True, blank=True)
    mostra = models.BooleanField(choices=DISPONIVEL_CHOICES, default=True, null=True, blank=True)
    def __str__(self):
        return f"Resultado - {self.doutora_responsavel.nome} - {self.assunto}"
