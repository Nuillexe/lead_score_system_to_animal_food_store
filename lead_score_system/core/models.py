from django.db import models

class Lead(models.Model):
    nome= models.CharField(max_length=100)
    idade=models.IntegerField()
    renda=models.DecimalField(max_digits=10, decimal_places=2)
    pontuacao=models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.nome} - Pontos: {self.pontuacao}"
    
    # Create your models here.
