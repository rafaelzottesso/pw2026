# 7. Síntese da Engenharia Reversa

## 7.1 Principais características arquiteturais

- Aplicação Django monolítica de app único (`website`), seguindo o padrão MTV (Model-Template-View) com Class-Based Views (`CreateView`, `UpdateView`, `DeleteView`, `ListView`, `DetailView`, `TemplateView`).
- Banco de dados relacional único (PostgreSQL) acessado via ORM do Django, sem camada de API/REST identificada.
- Autenticação e autorização baseadas no sistema nativo do Django, estendido por `django-braces` (`GroupRequiredMixin`) para controle por grupos em um recurso específico (Modalidade).
- Front-end server-side rendering (templates Django) com Bootstrap 5 via CDN e `django-crispy-forms` para formulários.
- Deploy sem servidor dedicado, voltado a Google App Engine (Gunicorn), com coleta de estáticos via `collectstatic` (`static_gcloud/`).
- Ferramenta de profiling (Django Debug Toolbar) integrada apenas para uso local.

## 7.2 Principais regras de negócio identificadas

- Propriedade de registro: usuários só podem editar/excluir os registros que criaram (`Jogador`, `Campeonato`, `Inscrição`, `Jogo`), implementada de forma consistente via `get_queryset()` sobrescrito em cada view.
- Controle por grupo apenas para Modalidade (`Administrador`/`Organizador` para criar/editar, `Administrador` para excluir) — é a única regra de autorização baseada em papel encontrada no sistema; as demais entidades usam apenas `LoginRequiredMixin` (qualquer usuário autenticado).
- Integridade referencial forte: quase todas as chaves estrangeiras usam `on_delete=PROTECT`, priorizando a preservação do histórico em vez da exclusão em cascata.
- Um jogo sempre relaciona duas inscrições (`time_1`, `time_2`) e, opcionalmente, um vencedor — mas essa regra de coerência (`vencedor` precisa ser um dos dois times) não é validada no código.

## 7.3 Principais pontos positivos

- Uso consistente de `select_related`/`prefetch_related` nas views mais relevantes, com atenção real a N+1 queries.
- Estrutura de views organizada, repetitiva de forma previsível (facilita manutenção e leitura).
- Mensagens de sucesso e feedback de UI bem integrados ao framework nativo de mensagens do Django.
- Comando de seed (`seed_demo_data`) idempotente, útil para desenvolvimento e demonstrações.
- Documentação operacional (`README.md`) já bastante detalhada sobre instalação, execução, deploy e otimizações — incomum e positivo para um projeto acadêmico.

## 7.4 Principais problemas ou riscos encontrados

- **Ausência total de testes automatizados** ([website/tests.py](../website/tests.py) vazio). É o risco mais crítico identificado: nenhuma regra de negócio, controle de acesso ou regra de propriedade possui rede de segurança automatizada.
- Falta de validação de coerência entre `Jogo.vencedor` e `Jogo.time_1`/`time_2` no nível de model/form.
- Ausência (não identificada) de criação automática dos grupos `Administrador`/`Organizador`, exigindo configuração manual em cada ambiente (risco operacional/deploy).
- Possível consulta `COUNT` redundante nos templates de listagem (`object_list.count`), não medida, mas identificada como ponto de investigação de desempenho.
- Dependências instaladas mas aparentemente não utilizadas no código (`django-filter`, `django-autocomplete-light`), o que pode indicar funcionalidade planejada e não implementada, ou dependência residual.
- Nenhuma métrica de desempenho real (Debug Toolbar) foi registrada no repositório; toda a análise de desempenho desta documentação é baseada em inspeção estática de código, não em medições.

## 7.5 Principais lacunas de documentação

- Não existe documento de requisitos original, casos de uso ou modelagem de negócio anterior a esta engenharia reversa.
- Não há descrição formal dos perfis de usuário (além do que pode ser inferido de `GroupRequiredMixin`/`LoginRequiredMixin`).
- Não há documentação sobre como os grupos `Administrador`/`Organizador` devem ser criados/atribuídos em um novo ambiente.
- Não há registros de decisões arquiteturais (ADR) explicando escolhas como PostgreSQL, Google App Engine ou a ausência de uma API.

## 7.6 Sugestões de melhoria

1. Implementar testes automatizados priorizando: regras de propriedade (RN01–RN04), controle de acesso por grupo (RN05), e a view `MeusJogos`.
2. Adicionar validação de domínio garantindo que `Jogo.vencedor` seja `time_1` ou `time_2` (via `clean()` no model ou validação no `ModelForm`).
3. Automatizar a criação dos grupos `Administrador`/`Organizador` (ex.: `data migration` ou comando de management dedicado), reduzindo dependência de configuração manual.
4. Validar com o Django Debug Toolbar, em ambiente de desenvolvimento, o impacto real de `{{ object_list.count }}` nas listagens e considerar substituir por `page_obj.paginator.count`.
5. Revisar a real necessidade de `django-filter` e `django-autocomplete-light` no `requirements.txt`; remover se não utilizadas, ou implementar a funcionalidade planejada (ex.: filtros de busca nas listagens).
6. Formalizar, mesmo que de forma enxuta, os requisitos e regras de negócio já implementados (a base para isso foi produzida nesta documentação), para servir de referência a futuras manutenções.
