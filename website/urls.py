from django.urls import path
from .views import * # Importa tudo do views
# importar as views de autenticação do Django
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView
)
from django.contrib.auth.mixins import LoginRequiredMixin


class AuthenticatedPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    pass

urlpatterns = [
    # path("admin/", admin.site.urls),

    # Views de autenticação
    path("login/", LoginView.as_view(
        template_name = "website/form.html",
        extra_context = {
            "titulo": "Autenticação de Usuário",
            "botao": "Entrar"
        }
    ), name="login"),

    # View de Logout
    path("logout/", LogoutView.as_view(), name="logout"),

    # View para alterar a senha do usuário
    path("alterar-senha/", AuthenticatedPasswordChangeView.as_view(
        template_name = "website/form.html",
        extra_context = {
            "titulo": "Alterar Senha",
            "botao": "Alterar"
        }
    ), name="alterar_senha"),

    path("", Index.as_view(), name="pagina_inicial"),
    path("sobre/", Sobre.as_view(), name="sobre"),
    path("contato/", Contato.as_view(), name="contato"),

    # URLS para Modalidade
    path("cadastrar/modalidade/", ModalidadeCreate.as_view(), name="modalidade_create"),
    path("listar/modalidades/", ModalidadeList.as_view(), name="modalidade_list"),
    path("editar/modalidade/<int:pk>/", ModalidadeUpdate.as_view(), name="modalidade_update"),
    path("excluir/modalidade/<int:pk>/", ModalidadeDelete.as_view(), name="modalidade_delete"),
    path("ver/modalidade/<int:pk>/", ModalidadeDetail.as_view(), name="modalidade_detail"),

    # URLS para Campus
    path("cadastrar/campus/", CampusCreate.as_view(), name="campus_create"),
    path("listar/campi/", CampusList.as_view(), name="campus_list"),
    path("editar/campus/<int:pk>/", CampusUpdate.as_view(), name="campus_update"),
    path("excluir/campus/<int:pk>/", CampusDelete.as_view(), name="campus_delete"),
    path("ver/campus/<int:pk>/", CampusDetail.as_view(), name="campus_detail"),

    # URLS para Fase
    path("cadastrar/fase/", FaseCreate.as_view(), name="fase_create"),
    path("listar/fases/", FaseList.as_view(), name="fase_list"),
    path("editar/fase/<int:pk>/", FaseUpdate.as_view(), name="fase_update"),
    path("excluir/fase/<int:pk>/", FaseDelete.as_view(), name="fase_delete"),
    path("ver/fase/<int:pk>/", FaseDetail.as_view(), name="fase_detail"),

    # URLS para Jogador
    path("cadastrar/jogador/", JogadorCreate.as_view(), name="jogador_create"),
    path("listar/jogadores/", JogadorList.as_view(), name="jogador_list"),
    path("editar/jogador/<int:pk>/", JogadorUpdate.as_view(), name="jogador_update"),
    path("excluir/jogador/<int:pk>/", JogadorDelete.as_view(), name="jogador_delete"),
    path("ver/jogador/<int:pk>/", JogadorDetail.as_view(), name="jogador_detail"),

    # URLS para Campeonato
    path("cadastrar/campeonato/", CampeonatoCreate.as_view(), name="campeonato_create"),
    path("listar/campeonatos/", CampeonatoList.as_view(), name="campeonato_list"),
    path("editar/campeonato/<int:pk>/", CampeonatoUpdate.as_view(), name="campeonato_update"),
    path("excluir/campeonato/<int:pk>/", CampeonatoDelete.as_view(), name="campeonato_delete"),
    path("ver/campeonato/<int:pk>/", CampeonatoDetail.as_view(), name="campeonato_detail"),

    # URLS para Inscrição
    path("cadastrar/inscricao/", InscricaoCreate.as_view(), name="inscricao_create"),
    path("listar/inscricoes/", InscricaoList.as_view(), name="inscricao_list"),
    path("editar/inscricao/<int:pk>/", InscricaoUpdate.as_view(), name="inscricao_update"),
    path("excluir/inscricao/<int:pk>/", InscricaoDelete.as_view(), name="inscricao_delete"),
    path("ver/inscricao/<int:pk>/", InscricaoDetail.as_view(), name="inscricao_detail"),

    # URLS para Jogo
    path("cadastrar/jogo/", JogoCreate.as_view(), name="jogo_create"),
    path("listar/jogos/", JogoList.as_view(), name="jogo_list"),
    path("meus-jogos/", MeusJogos.as_view(), name="meus_jogos"),
    path("editar/jogo/<int:pk>/", JogoUpdate.as_view(), name="jogo_update"),
    path("excluir/jogo/<int:pk>/", JogoDelete.as_view(), name="jogo_delete"),
    path("ver/jogo/<int:pk>/", JogoDetail.as_view(), name="jogo_detail"),

]
