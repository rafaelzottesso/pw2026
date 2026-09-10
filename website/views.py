from django.views.generic import TemplateView

# Importar as views para inserir, alterar e excluir
from django.views.generic.edit import CreateView, UpdateView, DeleteView
 
from django.views.generic.detail import DetailView # Ver/detalhar
from django.views.generic.list import ListView # Listar

# Importar a função que retorna a rota de uma URL
from django.urls import reverse_lazy
from django.db.models import Q
from django.db.models import Prefetch

# Importar as minhas classes do models.py
from .models import Campus, Modalidade, Fase, Jogador, Campeonato, Inscricao, Jogo

# Importar as MIxins para LOGIN
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from braces.views import GroupRequiredMixin

# Importar o mixin de mensagem de sucesso
from django.contrib.messages.views import SuccessMessageMixin


class SuccessMessageDeleteMixin(SuccessMessageMixin):
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        message = self.success_message % self.object.__dict__
        response = super().delete(request, *args, **kwargs)
        messages.success(request, message)
        return response


class Index(TemplateView):
    template_name = "website/inicio.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Adicionar os dados que quero enviar ao template
        # camp = NomeClasse.objects.filter(atributo1=valor)
        camp = (Campeonato.objects.select_related("campus")
            .prefetch_related("modalidades")
            .order_by("-cadastrado_em")[:5])
        context["campeonatos"] = camp
        inscricoes = (Inscricao.objects.select_related("campeonato", "modalidade")
            .order_by("-inscrito_em")[:5])
        context["inscricoes"] = inscricoes
        # Retorna o contexto com todos os dados mais o campeonato
        return context


class Sobre(TemplateView):
    template_name = "website/sobre.html"


class Contato(TemplateView):
    template_name = "website/contato.html"    


#################### Views para Modalidade ####################


class ModalidadeCreate(GroupRequiredMixin, SuccessMessageMixin, CreateView):
    group_required = ["Administrador","Organizador"]
    model = Modalidade
    fields = ["nome"]
    template_name = "website/form.html"
    success_url = reverse_lazy("modalidade_list")
    extra_context = {
        "titulo" : "Cadastro de Modalidades",
        "botao" : "Cadastrar"
    }
    success_message = "%(nome)s cadastrada com sucesso!"


class ModalidadeUpdate(GroupRequiredMixin, SuccessMessageMixin, UpdateView):
    group_required = ["Administrador","Organizador"]
    model = Modalidade
    fields = ["nome"]
    template_name = "website/form.html"
    success_url = reverse_lazy("modalidade_list")
    extra_context = {
        "titulo" : "Edição de Modalidades",
        "botao" : "Salvar"
    }
    success_message = "%(nome)s atualizada com sucesso!"


class ModalidadeDelete(GroupRequiredMixin, SuccessMessageDeleteMixin, DeleteView):
    group_required = ["Administrador"]
    model = Modalidade 
    template_name = "website/form.html"
    success_url = reverse_lazy("modalidade_list")
    extra_context = {
        "titulo" : "Excluir Modalidade",
        "botao" : "Excluir"
    }
    success_message = "%(nome)s excluída com sucesso!"


class ModalidadeList(LoginRequiredMixin, ListView):
    model = Modalidade
    template_name = "website/listas/modalidades.html"
    paginate_by = 20


class ModalidadeDetail(LoginRequiredMixin, DetailView):
    model = Modalidade
    template_name = "website/ver/modalidade.html"


#################### Views para Fase ####################

class FaseCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Fase
    fields = ["nome", "quantidade_jogos", "sequencia"]
    template_name = "website/form.html"
    success_url = reverse_lazy("fase_list")
    extra_context = {
        "titulo": "Cadastro de Fases",
        "botao": "Cadastrar"
    }
    success_message = "%(nome)s cadastrada com sucesso!"


class FaseUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Fase
    fields = ["nome", "quantidade_jogos", "sequencia"]
    template_name = "website/form.html"
    success_url = reverse_lazy("fase_list")
    extra_context = {
        "titulo": "Edição de Fases",
        "botao": "Salvar"
    }
    success_message = "%(nome)s atualizada com sucesso!"


class FaseDelete(LoginRequiredMixin, SuccessMessageDeleteMixin, DeleteView):
    model = Fase
    template_name = "website/form.html"
    success_url = reverse_lazy("fase_list")
    extra_context = {
        "titulo": "Excluir Fase",
        "botao": "Excluir"
    }
    success_message = "%(nome)s excluída com sucesso!"


class FaseList(LoginRequiredMixin, ListView):
    model = Fase
    template_name = "website/listas/fases.html"
    paginate_by = 20


class FaseDetail(DetailView):
    model = Fase
    template_name = "website/ver/fase.html"


#################### Views para Jogador ####################


class JogadorCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Jogador
    fields = ["nome", "telefone", "campus"]
    template_name = "website/form.html"
    success_url = reverse_lazy("jogador_list")
    extra_context = {
        "titulo": "Cadastro de Jogadores",
        "botao": "Cadastrar"
    }
    success_message = "%(nome)s cadastrado com sucesso!"

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)


class JogadorUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Jogador
    fields = ["nome", "telefone", "campus"]
    template_name = "website/form.html"
    success_url = reverse_lazy("jogador_list")
    extra_context = {
        "titulo": "Edição de Jogadores",
        "botao": "Salvar"
    }
    success_message = "%(nome)s atualizado com sucesso!"

    def get_queryset(self):
        return super().get_queryset().filter(usuario=self.request.user)


class JogadorDelete(LoginRequiredMixin, SuccessMessageDeleteMixin, DeleteView):
    model = Jogador
    template_name = "website/form.html"
    success_url = reverse_lazy("jogador_list")
    extra_context = {
        "titulo": "Excluir Jogador",
        "botao": "Excluir"
    }
    success_message = "%(nome)s excluído com sucesso!"

    def get_queryset(self):
        return super().get_queryset().filter(usuario=self.request.user)


class JogadorList(LoginRequiredMixin, ListView):
    model = Jogador
    template_name = "website/listas/jogadores.html"
    paginate_by = 50

    def get_queryset(self):
        return super().get_queryset().select_related("campus")


class JogadorDetail(DetailView):
    model = Jogador
    template_name = "website/ver/jogador.html"

    def get_queryset(self):
        return super().get_queryset().select_related("campus", "usuario")


#################### Views para Campeonato ####################


class CampeonatoCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Campeonato
    fields = ["nome", "categoria", "data_inicio", "data_limite_inscricao", "modalidades", "campus"]
    template_name = "website/form.html"
    success_url = reverse_lazy("campeonato_list")
    extra_context = {
        "titulo": "Cadastro de Campeonatos",
        "botao": "Cadastrar"
    }
    success_message = "%(nome)s cadastrado com sucesso!"
    # Obter o usuário que cadastrou o campeonato e definir o campo "cadastrado_por" automaticamente
    def form_valid(self, form):
        form.instance.cadastrado_por = self.request.user
        return super().form_valid(form)


class CampeonatoUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Campeonato
    fields = ["nome", "categoria", "data_inicio", "data_limite_inscricao", "modalidades", "campus"]
    template_name = "website/form.html"
    success_url = reverse_lazy("campeonato_list")
    extra_context = {
        "titulo": "Edição de Campeonatos",
        "botao": "Salvar"
    }
    success_message = "%(nome)s atualizado com sucesso!"

    # O método get_queryset é utilizado para filtrar o/os objetos dessa view
    # Utilizaremos ele para filtrar os registros do usuário
    def get_queryset(self):
        qs = super().get_queryset() # Obter o queryset original (todos os campeonatos)
        qs = qs.filter(cadastrado_por=self.request.user) # Filtrar apenas os campeonatos cadastrados pelo usuário logado
        return qs

class CampeonatoDelete(LoginRequiredMixin, SuccessMessageDeleteMixin, DeleteView):
    model = Campeonato
    template_name = "website/form.html"
    success_url = reverse_lazy("campeonato_list")
    extra_context = {
        "titulo": "Excluir Campeonato",
        "botao": "Excluir"
    }
    success_message = "%(nome)s excluído com sucesso!"

    # Filtrar apenas objetos do usuário logado
    def get_queryset(self):
        return super().get_queryset().filter(cadastrado_por=self.request.user)


class CampeonatoList(LoginRequiredMixin, ListView):
    model = Campeonato
    template_name = "website/listas/campeonatos.html"
    paginate_by = 20

    def get_queryset(self):
        return super().get_queryset().select_related("campus")

    # Filtrar apenas objetos do usuário logado
    # def get_queryset(self):
    #     return super().get_queryset().filter(cadastrado_por=self.request.user)


class CampeonatoDetail(DetailView):
    model = Campeonato
    template_name = "website/ver/campeonato.html"

    def get_queryset(self):
        return (super().get_queryset()
                .select_related("campus", "cadastrado_por")
                .prefetch_related(
                    "modalidades",
                    Prefetch(
                        "inscricao_set",
                        queryset=Inscricao.objects.select_related("modalidade"),
                    ),
                ))


#################### Views para Campus ####################


class CampusCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Campus
    fields = ["nome"]
    template_name = "website/form.html"
    success_url = reverse_lazy("campus_list")
    extra_context = {
        "titulo": "Cadastro de Campus",
        "botao": "Cadastrar"
    }
    success_message = "%(nome)s cadastrado com sucesso!"


class CampusUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Campus
    fields = ["nome"]
    template_name = "website/form.html"
    success_url = reverse_lazy("campus_list")
    extra_context = {
        "titulo": "Edição de Campus",
        "botao": "Salvar"
    }
    success_message = "%(nome)s atualizado com sucesso!"


class CampusDelete(LoginRequiredMixin, SuccessMessageDeleteMixin, DeleteView):
    model = Campus
    template_name = "website/form.html"
    success_url = reverse_lazy("campus_list")
    extra_context = {
        "titulo": "Excluir Campus",
        "botao": "Excluir"
    }
    success_message = "%(nome)s excluído com sucesso!"


class CampusList(LoginRequiredMixin, ListView):
    model = Campus
    template_name = "website/listas/campi.html"
    paginate_by = 50


class CampusDetail(DetailView):
    model = Campus
    template_name = "website/ver/campus.html"


#################### Views para Inscrição ####################


class InscricaoCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Inscricao
    fields = [
        "nome_time", "jogadores", "campeonato", 
        "modalidade", "confirmada",
        "confirmada_em" # remover o atributo "inscrito_por" pois será automático
    ]
    template_name = "website/form.html"
    success_url = reverse_lazy("inscricao_list")
    extra_context = {
        "titulo": "Cadastro de Inscrições",
        "botao": "Cadastrar"
    }
    success_message = "%(nome_time)s cadastrada com sucesso!"

    # Sobrescrever o método form_valid para atribuir o usuário logado ao campo "inscrito_por"
    def form_valid(self, form):
        # Aqui só tem os dados da instância do formulário
        form.instance.inscrito_por = self.request.user
        
        # Valida os dados, cria o objeto, salva no banco e retorna a URL de redirecionamento
        url = super().form_valid(form)

        # Consigo acessar o objeto criado
        # print(self.object)

        return url



class InscricaoUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Inscricao
    fields = ["nome_time", "jogadores", "campeonato", "modalidade", "confirmada", "confirmada_em"]
    template_name = "website/form.html"
    success_url = reverse_lazy("inscricao_list")
    extra_context = {
        "titulo": "Edição de Inscrições",
        "botao": "Salvar"
    }
    success_message = "%(nome_time)s atualizada com sucesso!"

    def get_queryset(self):
        return super().get_queryset().filter(inscrito_por=self.request.user)


class InscricaoDelete(LoginRequiredMixin, SuccessMessageDeleteMixin, DeleteView):
    model = Inscricao
    template_name = "website/form.html"
    success_url = reverse_lazy("inscricao_list")
    extra_context = {
        "titulo": "Excluir Inscrição",
        "botao": "Excluir"
    }
    success_message = "%(nome_time)s excluída com sucesso!"

    def get_queryset(self):
        return super().get_queryset().filter(inscrito_por=self.request.user)


class InscricaoList(LoginRequiredMixin, ListView):
    model = Inscricao
    template_name = "website/listas/inscricoes.html"
    paginate_by = 20

    def get_queryset(self):
        return super().get_queryset().select_related("campeonato", "modalidade")


class InscricaoDetail(DetailView):
    model = Inscricao
    template_name = "website/ver/inscricao.html"

    def get_queryset(self):
        return (super().get_queryset()
                .select_related(
                    "campeonato__campus",
                    "campeonato",
                    "modalidade",
                    "inscrito_por",
                )
                .prefetch_related(
                    Prefetch(
                        "jogadores",
                        queryset=Jogador.objects.select_related("campus"),
                    ),
                ))


#################### Views para Partida/Jogo ####################


class JogoCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Jogo
    fields = ["time_1", "time_2", "data_hora", "etapa", "modalidade", "vencedor", "resultado"]
    template_name = "website/form.html"
    success_url = reverse_lazy("jogo_list")
    extra_context = {
        "titulo": "Cadastro de Jogos",
        "botao": "Cadastrar"
    }
    success_message = "Jogo de %(data_hora)s cadastrado com sucesso!"

    # Obter o usuário que cadastrou o campeonato e definir o campo "cadastrado_por" automaticamente
    def form_valid(self, form):
        form.instance.cadastrado_por = self.request.user
        return super().form_valid(form)


class JogoUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Jogo
    fields = ["time_1", "time_2", "data_hora", "etapa", "modalidade", "vencedor", "resultado"]
    template_name = "website/form.html"
    success_url = reverse_lazy("jogo_list")
    extra_context = {
        "titulo": "Edição de Jogos",
        "botao": "Salvar"
    }
    success_message = "Jogo de %(data_hora)s atualizado com sucesso!"

    def get_queryset(self):
        return super().get_queryset().filter(cadastrado_por=self.request.user)


class JogoDelete(LoginRequiredMixin, SuccessMessageDeleteMixin, DeleteView):
    model = Jogo
    template_name = "website/form.html"
    success_url = reverse_lazy("jogo_list")
    extra_context = {
        "titulo": "Excluir Jogo",
        "botao": "Excluir"
    }
    success_message = "Jogo de %(data_hora)s excluído com sucesso!"

    def get_queryset(self):
        return super().get_queryset().filter(cadastrado_por=self.request.user)


class JogoList(LoginRequiredMixin, ListView):
    model = Jogo
    template_name = "website/listas/jogos.html"
    paginate_by = 20

    def get_queryset(self):
        return (super().get_queryset()
                .select_related("time_1", "time_2", "etapa", "modalidade"))


class MeusJogos(LoginRequiredMixin, ListView):
    model = Jogo
    template_name = "website/listas/jogos.html"
    paginate_by = 40

    def get_queryset(self):
        return (Jogo.objects
            .filter(Q(time_1__jogadores__usuario=self.request.user)
                | Q(time_2__jogadores__usuario=self.request.user))
            .select_related("time_1", "time_2", "etapa", "modalidade")
            .distinct())


class JogoDetail(DetailView):
    model = Jogo
    template_name = "website/ver/jogo.html"

    def get_queryset(self):
        return (super().get_queryset()
                .select_related(
                    "time_1__campeonato__campus",
                    "time_1__modalidade",
                    "time_2__campeonato__campus",
                    "time_2__modalidade",
                    "etapa",
                    "modalidade",
                    "vencedor",
                    "cadastrado_por",
                )
                .prefetch_related(
                    Prefetch(
                        "time_1__jogadores",
                        queryset=Jogador.objects.select_related("campus"),
                    ),
                    Prefetch(
                        "time_2__jogadores",
                        queryset=Jogador.objects.select_related("campus"),
                    ),
                ))
