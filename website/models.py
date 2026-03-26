from django.db import models

# Create your models here.
class Modalidade(models.Model):
    nome = models.CharField(max_length=30)

class Fase(models.Model):
    nome = models.CharField(max_length=30, help_text="Por exemplo: Final, Semi final, etc.")
    quantidade_jogos = models.PositiveSmallIntegerField(verbose_name='quantidade de jogos')
    sequencia = models.PositiveSmallIntegerField(verbose_name='sequência')

class Jogador(models.Model):
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=15, blank=True, default="")
    campus = models.CharField(max_length=30)

    usuario = models.OneToOneField('auth.User', on_delete=models.CASCADE)

    atualizado_em = models.DateTimeField(auto_now=True)
    cadastrado_em = models.DateTimeField(auto_now_add=True)
