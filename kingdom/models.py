from django.db import models

class NovoTestamento(models.Model):
    id = models.IntegerField(primary_key=True)
    livro = models.CharField(max_length=100)
    abreviacao = models.CharField(max_length=10)
