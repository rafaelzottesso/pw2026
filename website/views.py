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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Adicionar os dados que quero enviar ao template
        # camp = NomeClasse.objects.filter(atributo1=valor)
        camp = Campeonato.objects.all().order_by("-cadastrado_em")[:5]
        context["campeonatos"] = camp
        # Retorna o contexto com todos os dados mais o campeonato
        return context


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
    fields = ["nome", "telefone", "campus"]
    template_name = "website/form.html"
    success_url = reverse_lazy("jogador_list")
    extra_context = {
        "titulo": "Cadastro de Jogadores",
        "botao": "Cadastrar"
    }

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)


class JogadorUpdate(LoginRequiredMixin, UpdateView):
    model = Jogador
    fields = ["nome", "telefone", "campus"]
    template_name = "website/form.html"
    success_url = reverse_lazy("jogador_list")
    extra_context = {
        "titulo": "Edição de Jogadores",
        "botao": "Salvar"
    }

    def get_queryset(self):
        return super().get_queryset().filter(usuario=self.request.user)


class JogadorDelete(LoginRequiredMixin, DeleteView):
    model = Jogador
    template_name = "website/form.html"
    success_url = reverse_lazy("jogador_list")
    extra_context = {
        "titulo": "Excluir Jogador",
        "botao": "Excluir"
    }

    def get_queryset(self):
        return super().get_queryset().filter(usuario=self.request.user)


class JogadorList(LoginRequiredMixin, ListView):
    model = Jogador
    template_name = "website/listas/jogadores.html"


class JogadorDetail(DetailView):
    model = Jogador
    template_name = "website/ver/jogador.html"


#################### Views para Campeonato ####################


class CampeonatoCreate(LoginRequiredMixin, CreateView):
    model = Campeonato
    fields = ["nome", "categoria", "data_inicio", "data_limite_inscricao", "modalidades", "campus"]
    template_name = "website/form.html"
    success_url = reverse_lazy("campeonato_list")
    extra_context = {
        "titulo": "Cadastro de Campeonatos",
        "botao": "Cadastrar"
    }
    # Obter o usuário que cadastrou o campeonato e definir o campo "cadastrado_por" automaticamente
    def form_valid(self, form):
        form.instance.cadastrado_por = self.request.user
        return super().form_valid(form)


class CampeonatoUpdate(LoginRequiredMixin, UpdateView):
    model = Campeonato
    fields = ["nome", "categoria", "data_inicio", "data_limite_inscricao", "modalidades", "campus"]
    template_name = "website/form.html"
    success_url = reverse_lazy("campeonato_list")
    extra_context = {
        "titulo": "Edição de Campeonatos",
        "botao": "Salvar"
    }

    # O método get_queryset é utilizado para filtrar o/os objetos dessa view
    # Utilizaremos ele para filtrar os registros do usuário
    def get_queryset(self):
        qs = super().get_queryset() # Obter o queryset original (todos os campeonatos)
        qs = qs.filter(cadastrado_por=self.request.user) # Filtrar apenas os campeonatos cadastrados pelo usuário logado
        return qs

class CampeonatoDelete(LoginRequiredMixin, DeleteView):
    model = Campeonato
    template_name = "website/form.html"
    success_url = reverse_lazy("campeonato_list")
    extra_context = {
        "titulo": "Excluir Campeonato",
        "botao": "Excluir"
    }

    # Filtrar apenas objetos do usuário logado
    def get_queryset(self):
        return super().get_queryset().filter(cadastrado_por=self.request.user)


class CampeonatoList(LoginRequiredMixin, ListView):
    model = Campeonato
    template_name = "website/listas/campeonatos.html"
    paginate_by = 50

    # Filtrar apenas objetos do usuário logado
    # def get_queryset(self):
    #     return super().get_queryset().filter(cadastrado_por=self.request.user)


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

    # Sobrescrever o método form_valid para atribuir o usuário logado ao campo "inscrito_por"
    def form_valid(self, form):
        # Aqui só tem os dados da instância do formulário
        form.instance.inscrito_por = self.request.user
        
        # Valida os dados, cria o objeto, salva no banco e retorna a URL de redirecionamento
        url = super().form_valid(form)

        # Consigo acessar o objeto criado
        # print(self.object)

        return url



class InscricaoUpdate(LoginRequiredMixin, UpdateView):
    model = Inscricao
    fields = ["nome_time", "jogadores", "campeonato", "modalidade", "confirmada", "confirmada_em"]
    template_name = "website/form.html"
    success_url = reverse_lazy("inscricao_list")
    extra_context = {
        "titulo": "Edição de Inscrições",
        "botao": "Salvar"
    }

    def get_queryset(self):
        return super().get_queryset().filter(inscrito_por=self.request.user)


class InscricaoDelete(LoginRequiredMixin, DeleteView):
    model = Inscricao
    template_name = "website/form.html"
    success_url = reverse_lazy("inscricao_list")
    extra_context = {
        "titulo": "Excluir Inscrição",
        "botao": "Excluir"
    }

    def get_queryset(self):
        return super().get_queryset().filter(inscrito_por=self.request.user)


class InscricaoList(LoginRequiredMixin, ListView):
    model = Inscricao
    template_name = "website/listas/inscricoes.html"


class InscricaoDetail(DetailView):
    model = Inscricao
    template_name = "website/ver/inscricao.html"


#################### Views para Partida/Jogo ####################


class JogoCreate(LoginRequiredMixin, CreateView):
    model = Jogo
    fields = ["time_1", "time_2", "data_hora", "etapa", "modalidade", "vencedor", "resultado"]
    template_name = "website/form.html"
    success_url = reverse_lazy("jogo_list")
    extra_context = {
        "titulo": "Cadastro de Jogos",
        "botao": "Cadastrar"
    }

    # Obter o usuário que cadastrou o campeonato e definir o campo "cadastrado_por" automaticamente
    def form_valid(self, form):
        form.instance.cadastrado_por = self.request.user
        return super().form_valid(form)


class JogoUpdate(LoginRequiredMixin, UpdateView):
    model = Jogo
    fields = ["time_1", "time_2", "data_hora", "etapa", "modalidade", "vencedor", "resultado"]
    template_name = "website/form.html"
    success_url = reverse_lazy("jogo_list")
    extra_context = {
        "titulo": "Edição de Jogos",
        "botao": "Salvar"
    }

    def get_queryset(self):
        return super().get_queryset().filter(cadastrado_por=self.request.user)


class JogoDelete(LoginRequiredMixin, DeleteView):
    model = Jogo
    template_name = "website/form.html"
    success_url = reverse_lazy("jogo_list")
    extra_context = {
        "titulo": "Excluir Jogo",
        "botao": "Excluir"
    }

    def get_queryset(self):
        return super().get_queryset().filter(cadastrado_por=self.request.user)


class JogoList(LoginRequiredMixin, ListView):
    model = Jogo
    template_name = "website/listas/jogos.html"


class MeusJogos(LoginRequiredMixin, ListView):
    model = Jogo
    template_name = "website/listas/jogos.html"

    def get_queryset(self):
        jogadores_do_usuario = Jogador.objects.filter(usuario=self.request.user)

        queryset = Jogo.objects.filter(time_1__jogadores__in=jogadores_do_usuario).distinct()
        queryset |= Jogo.objects.filter(time_2__jogadores__in=jogadores_do_usuario).distinct()

        return queryset


class JogoDetail(DetailView):
    model = Jogo
    template_name = "website/ver/jogo.html"
