from django.db import models
from django.contrib import admin
from django.contrib import contenttypes

class Momentos(models.Model):
    nome = models.CharField(max_length=80,default="momento")
    momento = models.CharField(max_length=3000,default="um momento especial na minha vida")
    # permite um formato personalizado por usuario (02/02/24, fevereiro,02 de 2026, 2026/02/02)
    # sem quebrar a logica
    data = models.CharField(max_length=20,default="02 fev 2024")

    def __str__(self):
        return self.nome

class Filmes(models.Model):
    nome = models.CharField(max_length=80,default="filme")
    filme = models.FileField(upload_to="filmes/")
    data = models.CharField(max_length=20,default="02 fev 2024")

    def __str__(self):
        return self.nome

class Temporada(models.Model):
    nome = models.CharField(max_length=80,default="temporada 1")
    episodio_filme = models.ManyToManyField('Filmes',blank=True)
    episodio_momento = models.ManyToManyField('Momentos',blank=True)
    data = models.CharField(max_length=20,default="02 fev 2024")

    def __str__(self):
        return self.nome

class Serie(models.Model):
    nome = models.CharField(max_length=80,default="Minha serie")
    temporada = models.ManyToManyField('Temporada',blank=False)
    data = models.CharField(max_length=20,default="02 fev 2024")

    def __str__(self):
        return self.nome
