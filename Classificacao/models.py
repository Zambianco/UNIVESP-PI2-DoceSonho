from django.conf import settings
from django.db import models

class Categoria(models.Model):
    nomeCategoria = models.CharField(max_length=100)

    def publish(self):
        self.save()

    def __str__(self):
        return self.nomeCategoria

