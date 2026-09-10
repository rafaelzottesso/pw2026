# 1. Visão Geral

## Objetivo geral

Sistema web para gerenciamento de campeonatos de eSports acadêmicos, permitindo cadastro de campi, modalidades, fases de competição, jogadores, campeonatos, inscrições de times e jogos/partidas. Evidência: descrição do [README.md](../README.md) ("Sistema Django para gerenciamento de campeonatos de eSports, modalidades, campi, jogadores, inscrições e jogos.") e conjunto de models em [website/models.py](../website/models.py).

## Objetivos específicos

Inferidos a partir das entidades e views implementadas ([website/models.py](../website/models.py), [website/views.py](../website/views.py)):

- Manter um cadastro de campi (unidades/polos) participantes ([Campus](../website/models.py)).
- Manter um cadastro de modalidades de eSports (ex.: CS 2, LOL) ([Modalidade](../website/models.py), reforçado pelos dados de exemplo em [seed_demo_data.py](../website/management/commands/seed_demo_data.py)).
- Organizar campeonatos por categoria, período de inscrição e campus sede (`Campeonato`).
- Controlar inscrições de times (`Inscricao`), vinculando jogadores, campeonato e modalidade.
- Registrar jogos/partidas entre times inscritos, associados a uma fase (`Jogo`, `Fase`).
- Vincular jogadores a uma conta de usuário (`Jogador.usuario`, `OneToOneField`), permitindo que cada jogador acompanhe suas próprias partidas (view `MeusJogos`).
- Fornecer autenticação, mensagens de sucesso e navegação orientada a papéis (grupos `Administrador`/`Organizador`).

## Problema que o sistema resolve

Centralizar, em uma única aplicação, a organização de campeonatos multi-campus de eSports que hoje dependeria de controles dispersos (planilhas, grupos de mensagens etc.). O sistema oferece cadastro estruturado de entidades relacionadas (campus, modalidades, fases, jogadores, campeonatos, inscrições e jogos) com controle de acesso e histórico de cadastro/atualização (campos `cadastrado_em`, `atualizado_em`, `cadastrado_por`). Esta é uma inferência baseada na modelagem de dados; não há um documento de requisitos original no repositório que descreva o problema de negócio de forma explícita (**não identificado**).

## Principais usuários

Inferidos a partir de `LoginRequiredMixin`/`GroupRequiredMixin` em [website/views.py](../website/views.py) e do menu em [website/templates/website/modelo.html](../website/templates/website/modelo.html):

- **Visitante não autenticado**: acessa página inicial, "Sobre", "Contato" e páginas de detalhe não protegidas (`FaseDetail`, `CampeonatoDetail`, `CampusDetail`, `InscricaoDetail`, `JogoDetail` não usam `LoginRequiredMixin`).
- **Usuário autenticado comum (jogador)**: acessa cadastro/edição/exclusão de Campus, Fase, Jogador (próprio), Campeonato (próprio), Inscrição (própria) e Jogo (próprio), além da tela "Meus Jogos".
- **Organizador** (grupo `Administrador` ou `Organizador`): pode cadastrar/editar Modalidades (`ModalidadeCreate`, `ModalidadeUpdate` usam `group_required = ["Administrador","Organizador"]`).
- **Administrador** (grupo `Administrador`): único grupo autorizado a excluir Modalidades (`ModalidadeDelete.group_required = ["Administrador"]`); também administra dados via Django Admin ([website/admin.py](../website/admin.py)), o que exige `is_staff`/`is_superuser` (padrão do Django).

Não foi encontrado no repositório um cadastro explícito dos grupos `Administrador`/`Organizador` (são esperados via Django Admin/fixtures externas) — **não identificado** onde esses grupos são criados automaticamente.

## Principais funcionalidades

- CRUD completo (criar, listar, ver, editar, excluir) para: Modalidade, Fase, Jogador, Campeonato, Campus, Inscrição, Jogo ([website/views.py](../website/views.py), [website/urls.py](../website/urls.py)).
- Autenticação: login, logout e alteração de senha (`LoginView`, `LogoutView`, `PasswordChangeView` em [website/urls.py](../website/urls.py)).
- Mensagens de sucesso (framework `django.contrib.messages`) após criar/editar/excluir e após login, exibidas como toasts no template base ([website/templates/website/modelo.html](../website/templates/website/modelo.html)).
- Página inicial com os 5 campeonatos e as 5 inscrições mais recentes (`Index.get_context_data`).
- Tela "Meus Jogos", listando partidas em que o usuário logado participa como jogador de algum dos dois times (`MeusJogos`, uso de `Q()` e `distinct()`).
- Listagens paginadas (`paginate_by` de 20 a 50 itens) com paginação reutilizável ([website/templates/website/includes/pagination.html](../website/templates/website/includes/pagination.html), [website/templatetags/pagination.py](../website/templatetags/pagination.py)).
- Comando de gestão `seed_demo_data` para popular dados de demonstração de forma idempotente ([website/management/commands/seed_demo_data.py](../website/management/commands/seed_demo_data.py)).
- Painel administrativo padrão do Django com todos os models registrados ([website/admin.py](../website/admin.py)).

## Tecnologias utilizadas

Evidência em [requirements.txt](../requirements.txt), [pw2026/settings.py](../pw2026/settings.py) e [app.yaml](../app.yaml):

| Categoria | Tecnologia |
|---|---|
| Linguagem/Framework | Python 3.12, Django 5.2.13 |
| Banco de dados | PostgreSQL (via `psycopg2`), configurado por `DATABASE_URL` em `settings.py` |
| Controle de acesso por grupo | `django-braces` (`GroupRequiredMixin`) |
| Formulários | `django-crispy-forms` + `crispy-bootstrap5` |
| Filtros | `django-filter` (dependência instalada; uso efetivo em views/templates **não identificado**) |
| Ferramentas de desenvolvimento | `django-debug-toolbar`, `django-extensions` |
| Front-end | Bootstrap 5.3.3 e Bootstrap Icons via CDN, CSS customizado (`static/css/estilo.css`) |
| Servidor de aplicação | Gunicorn (`app.yaml`) |
| Hospedagem/deploy | Google App Engine (runtime `python312`, `app.yaml`) |
| Autocomplete | `django-autocomplete-light` (dependência instalada; uso efetivo em views/forms **não identificado**) |

`django-filter` e `django-autocomplete-light` estão listados em `requirements.txt`, mas não foram encontradas referências de uso (imports, `INSTALLED_APPS`, filtros em views) em `website/views.py` ou `website/urls.py` — **não foi possível confirmar seu uso efetivo** no código atual.
