from django.db import models
from django.utils import timezone
from .Fabricante import Fabricante
from .Categoria import Categoria


class Produto(models.Model):
    nome = models.CharField(max_length=200)
    destaque = models.BooleanField(default=False)
    promocao = models.BooleanField(default=False)
    mensagem_promocao = models.CharField(max_length=255, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    fabricante = models.ForeignKey(Fabricante, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='produtos/', null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
