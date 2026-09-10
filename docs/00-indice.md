# Documentação Técnica — Arena eSports (Engenharia Reversa)

> Documentação gerada por engenharia reversa do código-fonte, configurações e estrutura do projeto Django "pw2026" (Arena eSports). Todo o conteúdo é derivado de evidências encontradas no repositório. Itens que não puderam ser confirmados estão marcados como **não identificado** ou **não foi possível inferir**.

## Sumário

1. [Visão geral](01-visao-geral.md)
2. [Requisitos (RF, RNF, RN)](02-requisitos.md)
3. [UML e arquitetura](03-arquitetura-uml.md)
4. [Testes](04-testes.md)
5. [Desempenho](05-desempenho.md)
6. [Matriz de rastreabilidade](06-rastreabilidade.md)
7. [Síntese da engenharia reversa](07-sintese.md)

## Escopo e método

- Análise estática do código-fonte: [website/models.py](../website/models.py), [website/views.py](../website/views.py), [website/urls.py](../website/urls.py), [website/admin.py](../website/admin.py), [website/tests.py](../website/tests.py), [website/templatetags/pagination.py](../website/templatetags/pagination.py), [website/management/commands/seed_demo_data.py](../website/management/commands/seed_demo_data.py).
- Análise de configuração: [pw2026/settings.py](../pw2026/settings.py), [requirements.txt](../requirements.txt), [app.yaml](../app.yaml).
- Análise do banco: migrações [website/migrations/0001_initial.py](../website/migrations/0001_initial.py) e [website/migrations/0002_campus_campeonato_campus_alter_jogador_campus_and_more.py](../website/migrations/0002_campus_campeonato_campus_alter_jogador_campus_and_more.py).
- Análise de templates em [website/templates/website/](../website/templates/website/) para confirmar dados exibidos e possíveis riscos de desempenho.
- Nenhuma alteração foi feita no código da aplicação durante esta análise.
