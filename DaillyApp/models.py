from django.db import models
from django.contrib import admin
from django.contrib import contenttypes

# Create your models here.
class Cliente (models.Model):
    nome = models.CharField(max_length=75)
    email = models.CharField(max_length=200)

    def nome (self):
        return print(self.nome)

    class Dados (models.Model):
        class Arquivo(models.Model):
            nome_arquivo = models.CharField(max_length=100)
            arquivo = models.FileField(upload_to='arquivos/') # Salva os arquivos na pasta 'arquivos/' dentro de STATIC_ROOT
#            imagem = models.ImageField(upload_to='imagens/') # Salva imagens na pasta 'imagens/' dentro de STATIC_ROOT

@admin.action(description='nome do cliente')
def client_nome (modeladmin,request,queryset):
    print(Cliente.nome)
    

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
