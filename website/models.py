from django.db import models

# Create your models here.

class Campus(models.Model):
    nome = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.nome}"


class Modalidade(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.nome}"


class Fase(models.Model):
    nome = models.CharField(max_length=30, help_text="Por exemplo: Final, Semi final, etc.")
    quantidade_jogos = models.PositiveSmallIntegerField(verbose_name='quantidade de jogos')
    sequencia = models.PositiveSmallIntegerField(verbose_name='sequência')

    def __str__(self):
        return f"{self.nome}"
    

class Jogador(models.Model):
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=15, blank=True, default="")
    campus = models.ForeignKey(Campus, on_delete=models.PROTECT)

    usuario = models.OneToOneField('auth.User', on_delete=models.CASCADE)

    atualizado_em = models.DateTimeField(auto_now=True)
    cadastrado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Rafael - (44)99999-9999
        return f"{self.nome} - {self.telefone}"


class Campeonato(models.Model):
    nome = models.CharField(max_length=60)
    categoria = models.CharField(max_length=20)
    data_inicio = models.DateTimeField(verbose_name="data de início")
    data_limite_inscricao = models.DateTimeField(verbose_name="limite de inscrições")
    modalidades = models.ManyToManyField(Modalidade) #como uma lista de modalidades
    campus = models.ForeignKey(Campus, on_delete=models.PROTECT)

    atualizado_em = models.DateTimeField(auto_now=True)
    cadastrado_em = models.DateTimeField(auto_now_add=True)

    cadastrado_por = models.ForeignKey('auth.User', on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nome} ({self.data_inicio})"


class Inscricao(models.Model):
    nome_time = models.CharField(max_length=60, verbose_name="Nome do time", help_text="Informe o nome do time, ex: Time Alpha")
    jogadores = models.ManyToManyField(Jogador)
    campeonato = models.ForeignKey(Campeonato, on_delete=models.PROTECT)
    modalidade = models.ForeignKey(Modalidade, on_delete=models.PROTECT)
     
    confirmada = models.BooleanField(default=False)
    confirmada_em = models.DateTimeField(null=True, blank=True)

    inscrito_em = models.DateTimeField(auto_now_add=True)
    inscrito_por = models.ForeignKey('auth.User', on_delete=models.PROTECT)

    def __str__(self):
        if self.confirmada:
            return f"{self.nome_time} ✅"
        else:
            return f"{self.nome_time} ❌"


class Jogo(models.Model):
    time_1 = models.ForeignKey(Inscricao, on_delete=models.PROTECT, related_name="time_1")
    time_2 = models.ForeignKey(Inscricao, on_delete=models.PROTECT, related_name="time_2")
    data_hora = models.DateTimeField(null=True, blank=True, verbose_name="data e hora do jogo", help_text="Informe a data e hora do jogo, ex: 2024-12-31 18:00")
    etapa = models.ForeignKey(Fase, on_delete=models.PROTECT)
    modalidade = models.ForeignKey(Modalidade, on_delete=models.PROTECT)
    
    vencedor = models.ForeignKey(Inscricao, on_delete=models.PROTECT, null=True, blank=True, related_name="vencedor")
    resultado = models.CharField(max_length=30, null=True, blank=True, verbose_name="resultado do jogo", help_text="Informe o resultado do jogo, ex: 2-1")

    atualizado_em = models.DateTimeField(auto_now=True)
    cadastrado_em = models.DateTimeField(auto_now_add=True)
    cadastrado_por = models.ForeignKey('auth.User', on_delete=models.PROTECT)

    def __str__(self):
        if self.resultado:
            return f"{self.data_hora} ({self.resultado})"
        else:
            return f"{self.data_hora}"