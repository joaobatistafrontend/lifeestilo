from django.db import models
from PIL import Image
import os

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

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        fixed_size = (800, 600)

        for field_name in ['imagem_antes', 'imagem_depois']:
            imagem = getattr(self, field_name)
            if imagem:
                path = imagem.path
                img = Image.open(path).convert('RGB')

                # CROP central proporcional para manter a imagem no tamanho exato
                img_ratio = img.width / img.height
                target_ratio = fixed_size[0] / fixed_size[1]

                if img_ratio > target_ratio:
                    # imagem é mais larga → corta nas laterais
                    new_width = int(img.height * target_ratio)
                    offset = (img.width - new_width) // 2
                    crop_box = (offset, 0, offset + new_width, img.height)
                else:
                    # imagem é mais alta → corta em cima/baixo
                    new_height = int(img.width / target_ratio)
                    offset = (img.height - new_height) // 2
                    crop_box = (0, offset, img.width, offset + new_height)

                img = img.crop(crop_box)
                img = img.resize(fixed_size, Image.Resampling.LANCZOS)
                img.save(path, format='JPEG', quality=90)
