from django.views.generic import TemplateView

# Importar as views para inserir, alterar e excluir
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.views.generic.detail import DetailView # Ver/detalhar
from django.views.generic.list import ListView # Listar

# Importar a função que retorna a rota de uma URL
from django.urls import reverse_lazy

# Importar as minhas classes do models.py
from .models import Modalidade, Fase, Jogador, Campeonato


class Index(TemplateView):
    template_name = "website/inicio.html"


class Sobre(TemplateView):
    template_name = "website/sobre.html"


class Contato(TemplateView):
    template_name = "website/contato.html"    


#################### Views para Modalidade ####################


class ModalidadeCreate(CreateView):
    model = Modalidade
    fields = ["nome"]
    template_name = "website/form.html"
    success_url = reverse_lazy("pagina_inicial")
    extra_context = {
        "titulo" : "Cadastro de Modalidades",
        "botao" : "Cadastrar"
    }


class ModalidadeUpdate(UpdateView):
    model = Modalidade
    fields = ["nome"]
    template_name = "website/form.html"
    success_url = reverse_lazy("pagina_inicial")
    extra_context = {
        "titulo" : "Edição de Modalidades",
        "botao" : "Salvar"
    }


class ModalidadeDelete(DeleteView):
    model = Modalidade
    template_name = "website/form.html"
    success_url = reverse_lazy("pagina_inicial")
    extra_context = {
        "titulo" : "Excluir Modalidade",
        "botao" : "Excluir"
    }


class ModalidadeList(ListView):
    model = Modalidade
    template_name = "website/listas/modalidades.html"


class ModalidadeDetail(DetailView):
    model = Modalidade
    template_name = "website/ver/modalidade.html"


#################### Views para Fase ####################

class FaseCreate(CreateView):
    model = Fase
    fields = ["nome", "quantidade_jogos", "sequencia"]
    template_name = "website/form.html"
    success_url = reverse_lazy("pagina_inicial")
    extra_context = {
        "titulo": "Cadastro de Fases",
        "botao": "Cadastrar"
    }


class FaseUpdate(UpdateView):
    model = Fase
    fields = ["nome", "quantidade_jogos", "sequencia"]
    template_name = "website/form.html"
    success_url = reverse_lazy("pagina_inicial")
    extra_context = {
        "titulo": "Edição de Fases",
        "botao": "Salvar"
    }


class FaseDelete(DeleteView):
    model = Fase
    template_name = "website/form.html"
    success_url = reverse_lazy("pagina_inicial")
    extra_context = {
        "titulo": "Excluir Fase",
        "botao": "Excluir"
    }


class FaseList(ListView):
    model = Fase
    template_name = "website/listas/fases.html"


class FaseDetail(DetailView):
    model = Fase
    template_name = "website/ver/fase.html"


#################### Views para Jogador ####################


class JogadorCreate(CreateView):
    model = Jogador
    fields = ["nome", "telefone", "campus", "usuario"]
    template_name = "website/form.html"
    success_url = reverse_lazy("pagina_inicial")
    extra_context = {
        "titulo": "Cadastro de Jogadores",
        "botao": "Cadastrar"
    }


class JogadorUpdate(UpdateView):
    model = Jogador
    fields = ["nome", "telefone", "campus", "usuario"]
    template_name = "website/form.html"
    success_url = reverse_lazy("pagina_inicial")
    extra_context = {
        "titulo": "Edição de Jogadores",
        "botao": "Salvar"
    }


class JogadorDelete(DeleteView):
    model = Jogador
    template_name = "website/form.html"
    success_url = reverse_lazy("pagina_inicial")
    extra_context = {
        "titulo": "Excluir Jogador",
        "botao": "Excluir"
    }


class JogadorList(ListView):
    model = Jogador
    template_name = "website/listas/jogadores.html"


class JogadorDetail(DetailView):
    model = Jogador
    template_name = "website/ver/jogador.html"


#################### Views para Campeonato ####################


class CampeonatoCreate(CreateView):
    model = Campeonato
    fields = ["nome", "categoria", "data_inicio", "data_limite_inscricao", "modalidades"]
    template_name = "website/form.html"
    success_url = reverse_lazy("pagina_inicial")
    extra_context = {
        "titulo": "Cadastro de Campeonatos",
        "botao": "Cadastrar"
    }


class CampeonatoUpdate(UpdateView):
    model = Campeonato
    fields = ["nome", "categoria", "data_inicio", "data_limite_inscricao", "modalidades"]
    template_name = "website/form.html"
    success_url = reverse_lazy("pagina_inicial")
    extra_context = {
        "titulo": "Edição de Campeonatos",
        "botao": "Salvar"
    }


class CampeonatoDelete(DeleteView):
    model = Campeonato
    template_name = "website/form.html"
    success_url = reverse_lazy("pagina_inicial")
    extra_context = {
        "titulo": "Excluir Campeonato",
        "botao": "Excluir"
    }


class CampeonatoList(ListView):
    model = Campeonato
    template_name = "website/listas/campeonatos.html"


class CampeonatoDetail(DetailView):
    model = Campeonato
    template_name = "website/ver/campeonato.html"


#################### Views para Inscrição ####################
#################### Views para Partida ####################
