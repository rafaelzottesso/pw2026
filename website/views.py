from django.views.generic import TemplateView

# Importar as views para inserir, alterar e excluir
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.views.generic.detail import DetailView # Ver/detalhar
from django.views.generic.list import ListView # Listar

# Importar a função que retorna a rota de uma URL
from django.urls import reverse_lazy

# Importar as minhas classes do models.py
from .models import Campus, Modalidade, Fase, Jogador, Campeonato, Inscricao, Jogo

# Importar as MIxins para LOGIN
from django.contrib.auth.mixins import LoginRequiredMixin

class Index(TemplateView):
    template_name = "website/inicio.html"


class Sobre(TemplateView):
    template_name = "website/sobre.html"


class Contato(TemplateView):
    template_name = "website/contato.html"    


#################### Views para Modalidade ####################


class ModalidadeCreate(LoginRequiredMixin, CreateView):
    model = Modalidade
    fields = ["nome"]
    template_name = "website/form.html"
    success_url = reverse_lazy("modalidade_list")
    extra_context = {
        "titulo" : "Cadastro de Modalidades",
        "botao" : "Cadastrar"
    }


class ModalidadeUpdate(LoginRequiredMixin, UpdateView):
    model = Modalidade
    fields = ["nome"]
    template_name = "website/form.html"
    success_url = reverse_lazy("modalidade_list")
    extra_context = {
        "titulo" : "Edição de Modalidades",
        "botao" : "Salvar"
    }


class ModalidadeDelete(LoginRequiredMixin, DeleteView):
    model = Modalidade
    template_name = "website/form.html"
    success_url = reverse_lazy("modalidade_list")
    extra_context = {
        "titulo" : "Excluir Modalidade",
        "botao" : "Excluir"
    }


class ModalidadeList(LoginRequiredMixin, ListView):
    model = Modalidade
    template_name = "website/listas/modalidades.html"


class ModalidadeDetail(LoginRequiredMixin, DetailView):
    model = Modalidade
    template_name = "website/ver/modalidade.html"


#################### Views para Fase ####################

class FaseCreate(LoginRequiredMixin, CreateView):
    model = Fase
    fields = ["nome", "quantidade_jogos", "sequencia"]
    template_name = "website/form.html"
    success_url = reverse_lazy("fase_list")
    extra_context = {
        "titulo": "Cadastro de Fases",
        "botao": "Cadastrar"
    }


class FaseUpdate(LoginRequiredMixin, UpdateView):
    model = Fase
    fields = ["nome", "quantidade_jogos", "sequencia"]
    template_name = "website/form.html"
    success_url = reverse_lazy("fase_list")
    extra_context = {
        "titulo": "Edição de Fases",
        "botao": "Salvar"
    }


class FaseDelete(LoginRequiredMixin, DeleteView):
    model = Fase
    template_name = "website/form.html"
    success_url = reverse_lazy("fase_list")
    extra_context = {
        "titulo": "Excluir Fase",
        "botao": "Excluir"
    }


class FaseList(LoginRequiredMixin, ListView):
    model = Fase
    template_name = "website/listas/fases.html"


class FaseDetail(DetailView):
    model = Fase
    template_name = "website/ver/fase.html"


#################### Views para Jogador ####################


class JogadorCreate(LoginRequiredMixin, CreateView):
    model = Jogador
    fields = ["nome", "telefone", "campus", "usuario"]
    template_name = "website/form.html"
    success_url = reverse_lazy("jogador_list")
    extra_context = {
        "titulo": "Cadastro de Jogadores",
        "botao": "Cadastrar"
    }


class JogadorUpdate(LoginRequiredMixin, UpdateView):
    model = Jogador
    fields = ["nome", "telefone", "campus", "usuario"]
    template_name = "website/form.html"
    success_url = reverse_lazy("jogador_list")
    extra_context = {
        "titulo": "Edição de Jogadores",
        "botao": "Salvar"
    }


class JogadorDelete(LoginRequiredMixin, DeleteView):
    model = Jogador
    template_name = "website/form.html"
    success_url = reverse_lazy("jogador_list")
    extra_context = {
        "titulo": "Excluir Jogador",
        "botao": "Excluir"
    }


class JogadorList(LoginRequiredMixin, ListView):
    model = Jogador
    template_name = "website/listas/jogadores.html"


class JogadorDetail(DetailView):
    model = Jogador
    template_name = "website/ver/jogador.html"


#################### Views para Campeonato ####################


class CampeonatoCreate(LoginRequiredMixin, CreateView):
    model = Campeonato
    fields = ["nome", "categoria", "data_inicio", "data_limite_inscricao", "modalidades", "campus", "cadastrado_por"]
    template_name = "website/form.html"
    success_url = reverse_lazy("campeonato_list")
    extra_context = {
        "titulo": "Cadastro de Campeonatos",
        "botao": "Cadastrar"
    }


class CampeonatoUpdate(LoginRequiredMixin, UpdateView):
    model = Campeonato
    fields = ["nome", "categoria", "data_inicio", "data_limite_inscricao", "modalidades", "campus", "cadastrado_por"]
    template_name = "website/form.html"
    success_url = reverse_lazy("campeonato_list")
    extra_context = {
        "titulo": "Edição de Campeonatos",
        "botao": "Salvar"
    }


class CampeonatoDelete(LoginRequiredMixin, DeleteView):
    model = Campeonato
    template_name = "website/form.html"
    success_url = reverse_lazy("campeonato_list")
    extra_context = {
        "titulo": "Excluir Campeonato",
        "botao": "Excluir"
    }


class CampeonatoList(LoginRequiredMixin, ListView):
    model = Campeonato
    template_name = "website/listas/campeonatos.html"
    paginate_by = 50


class CampeonatoDetail(DetailView):
    model = Campeonato
    template_name = "website/ver/campeonato.html"


#################### Views para Campus ####################


class CampusCreate(LoginRequiredMixin, CreateView):
    model = Campus
    fields = ["nome"]
    template_name = "website/form.html"
    success_url = reverse_lazy("campus_list")
    extra_context = {
        "titulo": "Cadastro de Campus",
        "botao": "Cadastrar"
    }


class CampusUpdate(LoginRequiredMixin, UpdateView):
    model = Campus
    fields = ["nome"]
    template_name = "website/form.html"
    success_url = reverse_lazy("campus_list")
    extra_context = {
        "titulo": "Edição de Campus",
        "botao": "Salvar"
    }


class CampusDelete(LoginRequiredMixin, DeleteView):
    model = Campus
    template_name = "website/form.html"
    success_url = reverse_lazy("campus_list")
    extra_context = {
        "titulo": "Excluir Campus",
        "botao": "Excluir"
    }


class CampusList(LoginRequiredMixin, ListView):
    model = Campus
    template_name = "website/listas/campi.html"


class CampusDetail(DetailView):
    model = Campus
    template_name = "website/ver/campus.html"


#################### Views para Inscrição ####################


class InscricaoCreate(LoginRequiredMixin, CreateView):
    model = Inscricao
    fields = ["nome_time", "jogadores", "campeonato", "modalidade", "confirmada", "confirmada_em", "inscrito_por"]
    template_name = "website/form.html"
    success_url = reverse_lazy("inscricao_list")
    extra_context = {
        "titulo": "Cadastro de Inscrições",
        "botao": "Cadastrar"
    }


class InscricaoUpdate(LoginRequiredMixin, UpdateView):
    model = Inscricao
    fields = ["nome_time", "jogadores", "campeonato", "modalidade", "confirmada", "confirmada_em", "inscrito_por"]
    template_name = "website/form.html"
    success_url = reverse_lazy("inscricao_list")
    extra_context = {
        "titulo": "Edição de Inscrições",
        "botao": "Salvar"
    }


class InscricaoDelete(LoginRequiredMixin, DeleteView):
    model = Inscricao
    template_name = "website/form.html"
    success_url = reverse_lazy("inscricao_list")
    extra_context = {
        "titulo": "Excluir Inscrição",
        "botao": "Excluir"
    }


class InscricaoList(LoginRequiredMixin, ListView):
    model = Inscricao
    template_name = "website/listas/inscricoes.html"


class InscricaoDetail(DetailView):
    model = Inscricao
    template_name = "website/ver/inscricao.html"


#################### Views para Partida/Jogo ####################


class JogoCreate(LoginRequiredMixin, CreateView):
    model = Jogo
    fields = ["time_1", "time_2", "data_hora", "etapa", "modalidade", "vencedor", "resultado", "cadastrado_por"]
    template_name = "website/form.html"
    success_url = reverse_lazy("jogo_list")
    extra_context = {
        "titulo": "Cadastro de Jogos",
        "botao": "Cadastrar"
    }


class JogoUpdate(LoginRequiredMixin, UpdateView):
    model = Jogo
    fields = ["time_1", "time_2", "data_hora", "etapa", "modalidade", "vencedor", "resultado", "cadastrado_por"]
    template_name = "website/form.html"
    success_url = reverse_lazy("jogo_list")
    extra_context = {
        "titulo": "Edição de Jogos",
        "botao": "Salvar"
    }


class JogoDelete(LoginRequiredMixin, DeleteView):
    model = Jogo
    template_name = "website/form.html"
    success_url = reverse_lazy("jogo_list")
    extra_context = {
        "titulo": "Excluir Jogo",
        "botao": "Excluir"
    }


class JogoList(LoginRequiredMixin, ListView):
    model = Jogo
    template_name = "website/listas/jogos.html"


class JogoDetail(DetailView):
    model = Jogo
    template_name = "website/ver/jogo.html"
