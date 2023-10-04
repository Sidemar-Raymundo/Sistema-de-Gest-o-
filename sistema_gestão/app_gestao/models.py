from django.db import models

# Create your models here.

from django.db import models

class AvaliacaoFilme(models.Model):
    id = models.AutoField(primary_key=True)
    filme = models.CharField(max_length=100)
    finalizado = models.BooleanField(default=False)
    resenha = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.filme
