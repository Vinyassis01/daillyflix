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
    