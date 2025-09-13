from django.db import models

# Create your models here.

class Estado(models.Model):
    nome = models.CharField(max_length=50)
    sigla = models.CharField(max_length=2, unique=True)
    regiao = models.CharField(max_length=20)
    descricao = models.TextField(blank=True, null=True)
    imagem = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.nome} ({self.sigla})"
    
class PontoTuristico(models.Model):
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, related_name="pontos")
    nome = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nome}"