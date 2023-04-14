from django.db import models

class NovoTestamento(models.Model):
    livro = models.CharField(max_length=100)
    abreviacao = models.CharField(max_length=10)
