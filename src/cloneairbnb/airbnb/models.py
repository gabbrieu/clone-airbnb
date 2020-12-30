from django.db import models
from django.contrib.postgres.fields import CIEmailField, CITextField

class Cliente(models.Model):
    cliente_nome = CITextField()
    cliente_email = CIEmailField()
    cliente_senha = models.CharField(max_length=50)

    def __str__(self):
        return self.cliente_nome
# Create your models here.
