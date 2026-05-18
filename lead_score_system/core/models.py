from django.db import models

class Lead(models.Model):
    email = models.EmailField()
    nome = models.CharField(max_length=150)
    renda = models.DecimalField(max_digits=10, decimal_places=2)
    idade = models.PositiveIntegerField()
    pontuacao=models.IntegerField(null=True, blank=True)
    
    prefere_saco_racao = models.BooleanField(
        verbose_name="Prefere comprar saco de ração?"
    )
    
    numero_pets = models.PositiveIntegerField()

    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} - {self.pontuacao}"

