from django.urls import path
from .views import Index, Sobre, Contato
from .views import * # Importa tudo do views

urlpatterns = [
    # path("admin/", admin.site.urls),

    path("", Index.as_view(), name="pagina_inicial"),
    path("sobre/", Sobre.as_view(), name="sobre"),
    path("contato/", Contato.as_view(), name="contato"),

    # URLS para Modalidade
    path("cadastrar/modalidade/", ModalidadeCreate.as_view(), name="modalidade_create"),
    path("listar/modalidades/", ModalidadeList.as_view(), name="modalidade_list"),
    path("editar/modalidade/<int:pk>/", ModalidadeUpdate.as_view(), name="modalidade_update"),
    path("excluir/modalidade/<int:pk>/", ModalidadeDelete.as_view(), name="modalidade_delete"),
    path("ver/modalidade/<int:pk>/", ModalidadeDetail.as_view(), name="modalidade_detail"),
]
