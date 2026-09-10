# 2. Requisitos

> Requisitos reconstruídos a partir do comportamento observado no código (views, urls, models, settings). Não existe documento de requisitos original no repositório; portanto, a redação abaixo é uma inferência de engenharia reversa, priorizando os itens mais sustentáveis pelas evidências.

## 2.1 Requisitos Funcionais (RF)

| ID | Descrição | Evidência |
|---|---|---|
| RF01 | O sistema deve permitir cadastrar, listar, visualizar, editar e excluir Campus. | `CampusCreate/List/Detail/Update/Delete` em [website/views.py](../website/views.py) |
| RF02 | O sistema deve permitir cadastrar, listar, visualizar, editar e excluir Modalidades, restringindo criação/edição aos grupos `Administrador`/`Organizador` e exclusão ao grupo `Administrador`. | `ModalidadeCreate/Update` (`group_required = ["Administrador","Organizador"]`), `ModalidadeDelete` (`group_required = ["Administrador"]`) em [website/views.py](../website/views.py) |
| RF03 | O sistema deve permitir cadastrar, listar, visualizar, editar e excluir Fases de campeonato (nome, quantidade de jogos, sequência). | `FaseCreate/List/Detail/Update/Delete` em [website/views.py](../website/views.py) |
| RF04 | O sistema deve permitir cadastrar, listar, visualizar, editar e excluir Jogadores, vinculando cada jogador a um usuário autenticado. | `JogadorCreate.form_valid` define `form.instance.usuario = self.request.user`; `JogadorUpdate/Delete` filtram por `usuario=self.request.user` |
| RF05 | O sistema deve permitir cadastrar, listar, visualizar, editar e excluir Campeonatos, registrando o usuário responsável pelo cadastro. | `CampeonatoCreate.form_valid` define `cadastrado_por`; `CampeonatoUpdate/Delete` filtram por `cadastrado_por=self.request.user` |
| RF06 | O sistema deve permitir cadastrar, listar, visualizar, editar e excluir Inscrições de times em campeonatos, associando jogadores e modalidade. | `InscricaoCreate/Update/Delete/List/Detail` em [website/views.py](../website/views.py); model `Inscricao` com `jogadores` (M2M) |
| RF07 | O sistema deve permitir cadastrar, listar, visualizar, editar e excluir Jogos (partidas) entre duas inscrições, associados a uma fase e modalidade. | `JogoCreate/Update/Delete/List/Detail` em [website/views.py](../website/views.py); model `Jogo` (`time_1`, `time_2`, `etapa`, `modalidade`) |
| RF08 | O sistema deve exibir ao usuário autenticado uma listagem de jogos em que ele participa como jogador de um dos dois times. | `MeusJogos.get_queryset` (filtro `Q(time_1__jogadores__usuario=...) \| Q(time_2__jogadores__usuario=...)`) |
| RF09 | O sistema deve autenticar usuários (login), permitir logout e alteração de senha. | Rotas `login/`, `logout/`, `alterar-senha/` em [website/urls.py](../website/urls.py) |
| RF10 | O sistema deve exibir mensagens de sucesso para o usuário após operações de criação, edição, exclusão e login. | `SuccessMessageMixin`, `SuccessMessageDeleteMixin`, `LoginSuccessView` em [website/views.py](../website/views.py) e [website/urls.py](../website/urls.py); bloco de toasts em [modelo.html](../website/templates/website/modelo.html) |
| RF11 | A página inicial deve exibir os campeonatos e as inscrições mais recentes. | `Index.get_context_data` (querysets ordenados por `-cadastrado_em`/`-inscrito_em`, limitados a 5) |
| RF12 | O sistema deve permitir popular dados de demonstração (campi, modalidades, fases, usuários, jogadores, campeonatos, inscrições e jogos) de forma reexecutável sem duplicação. | Comando `seed_demo_data` (uso de `get_or_create`/`update_or_create`) |
| RF13 | O sistema deve disponibilizar um painel administrativo para gestão direta de todos os models. | Todos os models registrados em [website/admin.py](../website/admin.py) |
| RF14 | As listagens devem ser paginadas. | `paginate_by` definido em todas as `ListView` (20 a 50 itens) |

## 2.2 Requisitos Não Funcionais (RNF)

| ID | Descrição | Evidência |
|---|---|---|
| RNF01 | A maioria das operações de escrita (criar/editar/excluir) deve exigir autenticação. | `LoginRequiredMixin` aplicado a praticamente todas as views de CRUD em [website/views.py](../website/views.py) |
| RNF02 | O sistema deve suportar controle de acesso baseado em grupos para operações sensíveis (Modalidade). | `GroupRequiredMixin` (pacote `django-braces`) |
| RNF03 | O sistema deve persistir dados em um SGBD relacional (PostgreSQL). | Configuração `DATABASES` com `django.db.backends.postgresql` e `psycopg2` em [pw2026/settings.py](../pw2026/settings.py) |
| RNF04 | O sistema deve ser implantável em ambiente de nuvem (Google App Engine) com servidor WSGI de múltiplas threads. | [app.yaml](../app.yaml) (`gunicorn ... --workers 1 --threads 6 --worker-class gthread`) |
| RNF05 | O sistema deve utilizar localização em português do Brasil e fuso horário de Brasília. | `LANGUAGE_CODE = "pt-br"`, `TIME_ZONE = "America/Sao_Paulo"` em `settings.py` |
| RNF06 | Consultas que envolvem relacionamentos devem ser otimizadas para reduzir o número de acessos ao banco. | Uso extensivo de `select_related`/`prefetch_related` em `website/views.py` (detalhado na seção de Desempenho) |
| RNF07 | Ferramentas de depuração de desempenho (Debug Toolbar) devem ficar restritas a ambientes de desenvolvimento local. | `INTERNAL_IPS = ["127.0.0.1"]` em `settings.py`; documentado também no [README.md](../README.md) |
| RNF08 | Formulários devem ser protegidos contra CSRF. | `{% csrf_token %}` presente nos templates de formulário ([form.html](../website/templates/website/form.html)) |
| RNF09 | Exclusões não devem comprometer a integridade referencial dos dados relacionados. | Praticamente todos os `ForeignKey` usam `on_delete=models.PROTECT` (ver `website/models.py` e migrações) |
| RNF10 | O sistema deve fornecer feedback visual de curta duração para mensagens de sistema, sem obstruir a navegação. | Toasts com `data-bs-delay="12000"` e posicionamento abaixo da navbar em [modelo.html](../website/templates/website/modelo.html) |

## 2.3 Regras de Negócio (RN)

| ID | Descrição | Evidência |
|---|---|---|
| RN01 | Um usuário só pode editar ou excluir os jogadores que ele mesmo cadastrou (vínculo 1:1 usuário–jogador). | `Jogador.usuario` é `OneToOneField`; `JogadorUpdate/Delete.get_queryset` filtram por `usuario=self.request.user` |
| RN02 | Um usuário só pode editar ou excluir os campeonatos que ele mesmo cadastrou. | `CampeonatoUpdate/Delete.get_queryset` filtram por `cadastrado_por=self.request.user` |
| RN03 | Um usuário só pode editar ou excluir as inscrições que ele mesmo realizou. | `InscricaoUpdate/Delete.get_queryset` filtram por `inscrito_por=self.request.user` |
| RN04 | Um usuário só pode editar ou excluir os jogos que ele mesmo cadastrou. | `JogoUpdate/Delete.get_queryset` filtram por `cadastrado_por=self.request.user` |
| RN05 | Somente usuários dos grupos `Administrador` ou `Organizador` podem cadastrar/editar Modalidades; somente `Administrador` pode excluí-las. | `group_required` em `ModalidadeCreate`, `ModalidadeUpdate`, `ModalidadeDelete` |
| RN06 | Não é permitido excluir um registro que ainda esteja referenciado por outro (Campus, Modalidade, Fase, Jogador, Campeonato, Inscrição), pois a exclusão é protegida no nível de banco de dados. | `on_delete=models.PROTECT` em praticamente todos os relacionamentos de `website/models.py` |
| RN07 | Um jogo é sempre disputado entre exatamente duas inscrições (`time_1` e `time_2`), podendo opcionalmente ter um vencedor entre as inscrições participantes. | Campos `time_1`, `time_2`, `vencedor` (`ForeignKey` para `Inscricao`) em `Jogo` |
| RN08 | Uma inscrição pode estar confirmada ou pendente, com data de confirmação registrada quando aplicável. | Campos `confirmada` (booleano) e `confirmada_em` (data/hora, opcional) em `Inscricao` |

Não foi encontrada, no código, validação que garanta `vencedor` ∈ {`time_1`, `time_2`} (ex.: `clean()`/`full_clean` customizado no model ou no form) — este é um ponto de regra de negócio **implícita mas não validada no código**, listado também na síntese final.
