# 6. Matriz de Rastreabilidade

Relaciona os principais requisitos funcionais às views/URLs/templates que os implementam. Nem todos os requisitos listados em [02-requisitos.md](02-requisitos.md) estão representados — foram priorizados os mais relevantes para a compreensão da arquitetura.

| Requisito | Caso de uso | Componente / Classe | Implementação (arquivo) |
|---|---|---|---|
| RF01 — CRUD Campus | Gerenciar Campus | `CampusCreate`, `CampusUpdate`, `CampusDelete`, `CampusList`, `CampusDetail` | [website/views.py](../website/views.py), rotas `*/campus/*` em [website/urls.py](../website/urls.py) |
| RF02 — CRUD Modalidade com RBAC | Gerenciar Modalidades | `ModalidadeCreate`, `ModalidadeUpdate`, `ModalidadeDelete` (`GroupRequiredMixin`) | [website/views.py](../website/views.py); grupos `Administrador`/`Organizador` |
| RF03 — CRUD Fase | Gerenciar Fases | `FaseCreate`, `FaseUpdate`, `FaseDelete`, `FaseList`, `FaseDetail` | [website/views.py](../website/views.py) |
| RF04 — CRUD Jogador (próprio) | Gerenciar Jogador | `JogadorCreate/Update/Delete/List/Detail` | [website/views.py](../website/views.py); `Jogador.usuario` (OneToOne) em [website/models.py](../website/models.py) |
| RF05 — CRUD Campeonato (próprio) | Gerenciar Campeonato | `CampeonatoCreate/Update/Delete/List/Detail` | [website/views.py](../website/views.py); `Campeonato.cadastrado_por` |
| RF06 — CRUD Inscrição (própria) | Gerenciar Inscrição | `InscricaoCreate/Update/Delete/List/Detail` | [website/views.py](../website/views.py); `Inscricao.inscrito_por`, `Inscricao.jogadores` (M2M) |
| RF07 — CRUD Jogo (próprio) | Gerenciar Jogo | `JogoCreate/Update/Delete/List/Detail` | [website/views.py](../website/views.py); `Jogo.time_1`/`time_2`/`vencedor` |
| RF08 — Meus Jogos | Ver Meus Jogos | `MeusJogos` | [website/views.py](../website/views.py); template [listas/jogos.html](../website/templates/website/listas/jogos.html) |
| RF09 — Autenticação | Autenticar-se / Alterar senha | `LoginSuccessView`, `LogoutView`, `AuthenticatedPasswordChangeView` | [website/urls.py](../website/urls.py) |
| RF10 — Mensagens de sucesso | Todos os casos de uso de CRUD e login | `SuccessMessageMixin`, `SuccessMessageDeleteMixin`, `LoginSuccessView.form_valid` | [website/views.py](../website/views.py), [website/urls.py](../website/urls.py); toasts em [modelo.html](../website/templates/website/modelo.html) |
| RF11 — Página inicial com dados recentes | Consultar página inicial | `Index` | [website/views.py](../website/views.py); template [inicio.html](../website/templates/website/inicio.html) |
| RF12 — Dados de demonstração | (uso administrativo, fora do fluxo web) | Comando `seed_demo_data` | [website/management/commands/seed_demo_data.py](../website/management/commands/seed_demo_data.py) |
| RF13 — Painel administrativo | Administrar dados via Admin | Registro de todos os models | [website/admin.py](../website/admin.py) |
| RF14 — Paginação | Todos os casos de uso de listagem | `paginate_by` + `{% include "website/includes/pagination.html" %}` | [website/views.py](../website/views.py), [includes/pagination.html](../website/templates/website/includes/pagination.html), [templatetags/pagination.py](../website/templatetags/pagination.py) |
| RN01–RN04 — Regras de "dono do registro" | Gerenciar Jogador/Campeonato/Inscrição/Jogo | `get_queryset()` sobrescrito em cada `UpdateView`/`DeleteView` | [website/views.py](../website/views.py) |
| RN06 — Integridade referencial | Todos os casos de exclusão | `on_delete=models.PROTECT` | [website/models.py](../website/models.py), migrações em [website/migrations/](../website/migrations/) |

Não foi encontrado um requisito ou caso de uso documentado para relatórios, dashboards analíticos, chaveamento automático de fases ou notificações externas (e-mail/push) — esses elementos, se existirem como necessidade de negócio, **não foram implementados no código analisado**.
