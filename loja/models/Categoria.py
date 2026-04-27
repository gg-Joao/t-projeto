from django.db import models
from django.utils import timezone


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
