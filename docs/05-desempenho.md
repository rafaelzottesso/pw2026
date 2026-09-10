# 5. Desempenho

## 5.1 Consultas otimizadas encontradas

O projeto já aplica `select_related` (para `ForeignKey`/`OneToOneField`) e `prefetch_related` (para `ManyToManyField` e relações reversas) em vários pontos de [website/views.py](../website/views.py):

| View | Otimização aplicada | Relação otimizada |
|---|---|---|
| `Index.get_context_data` | `select_related("campus")` + `prefetch_related("modalidades")` | Campeonatos recentes + suas modalidades |
| `Index.get_context_data` | `select_related("campeonato", "modalidade")` | Inscrições recentes |
| `JogadorList.get_queryset` | `select_related("campus")` | Campus do jogador |
| `JogadorDetail.get_queryset` | `select_related("campus", "usuario")` | Campus e usuário do jogador |
| `CampeonatoList.get_queryset` | `select_related("campus")` | Campus do campeonato |
| `CampeonatoDetail.get_queryset` | `select_related("campus", "cadastrado_por")` + `prefetch_related("modalidades", Prefetch("inscricao_set", ...))` | Modalidades e inscrições do campeonato |
| `InscricaoList.get_queryset` | `select_related("campeonato", "modalidade")` | Campeonato e modalidade da inscrição |
| `InscricaoDetail.get_queryset` | `select_related("campeonato__campus", "campeonato", "modalidade", "inscrito_por")` + `Prefetch("jogadores", ...)` | Cadeia campus→campeonato e jogadores do time |
| `JogoList.get_queryset` | `select_related("time_1", "time_2", "etapa", "modalidade")` | Times, fase e modalidade do jogo |
| `MeusJogos.get_queryset` | `select_related(...)` + `distinct()` | Evita duplicidade ao filtrar por `Q()` em `time_1`/`time_2` |
| `JogoDetail.get_queryset` | `select_related` (times, campus, modalidade, vencedor, cadastrado_por) + `Prefetch` para jogadores de cada time | Detalhe completo de uma partida |

Essas otimizações indicam preocupação deliberada com o problema de N+1 queries nas telas de listagem e detalhe mais "pesadas" (Campeonato, Inscrição, Jogo).

## 5.2 Pontos sem otimização explícita (investigar)

- `ModalidadeList`, `FaseList`, `CampusList`: não usam `select_related`/`prefetch_related`, mas os models `Modalidade`, `Fase` e `Campus` não possuem `ForeignKey` próprios, portanto o risco de N+1 nessas telas é baixo (**ponto de investigação de baixo risco**).
- Menu de navegação em [modelo.html](../website/templates/website/modelo.html) e `Index` (página inicial): a `Index` já usa `prefetch_related("modalidades")`, evitando N+1 ao iterar `camp.modalidades.all()` no template `inicio.html`. Esse é um exemplo positivo de mitigação encontrado.

## 5.3 Possível consulta redundante (COUNT duplicado em listagens)

Os templates de listagem (por exemplo, [listas/campeonatos.html](../website/templates/website/listas/campeonatos.html) e [listas/inscricoes.html](../website/templates/website/listas/inscricoes.html)) exibem o total de registros com `{{ object_list.count }}`:

```html
<p class="text-muted small mb-0">Total de {{ object_list.count }} campeonatos registrados.</p>
```

Como as views são `ListView` com `paginate_by` definido, o Django já calcula a contagem total via `paginator.count` para exibir a paginação. Chamar `object_list.count()` novamente no template executa uma consulta `COUNT(*)` adicional (o `object_list` de uma `ListView` paginada corresponde aos itens da página atual, não ao total). **Ponto de investigação**: confirmar, com o Django Debug Toolbar, se essa chamada gera uma query extra por requisição e se o valor exibido corresponde de fato ao total desejado (total geral vs. total da página).

## 5.4 Operações potencialmente custosas

- `MeusJogos.get_queryset` usa `Q(time_1__jogadores__usuario=...) | Q(time_2__jogadores__usuario=...)` combinado com `.distinct()`. Consultas com `OR` sobre relações `ManyToMany` seguidas de `distinct()` podem gerar `JOIN`s custosos em tabelas grandes. Não há paginação de índice adicional (apenas `paginate_by = 40`) nem cache. **Ponto de investigação de desempenho conforme a base de dados cresce.**
- `seed_demo_data` executa múltiplas operações `get_or_create`/`update_or_create` dentro de uma única transação (`transaction.atomic()`), o que é adequado para consistência, mas pode ser lento em bases muito grandes (**baixo risco**, comando administrativo, não é executado em requisições de usuário).

## 5.5 Uso do Django Debug Toolbar

A ferramenta está instalada e configurada:

- Dependência: `django-debug-toolbar==6.1.0` em [requirements.txt](../requirements.txt).
- Registrada em `INSTALLED_APPS` e `MIDDLEWARE` em [pw2026/settings.py](../pw2026/settings.py).
- Rota habilitada em [pw2026/urls.py](../pw2026/urls.py) (`path('__debug__/', include('debug_toolbar.urls'))`).
- Restrita a `INTERNAL_IPS = ["127.0.0.1"]`, ou seja, só aparece em acesso local durante desenvolvimento.

**Não foram encontrados registros, prints, capturas de tela ou relatórios no repositório com resultados reais do Debug Toolbar** (número de queries, tempo de resposta, etc.). Portanto, nenhuma métrica de desempenho medida é apresentada nesta documentação — todos os pontos acima são **hipóteses a validar**, não medições.

### Como validar os pontos levantados

1. Acessar as telas de listagem e detalhe (`/listar/campeonatos/`, `/ver/campeonato/<id>/`, `/listar/jogos/`, `/meus-jogos/`) localmente via `127.0.0.1:8000`.
2. Observar no painel do Debug Toolbar (aba "SQL") o número de queries disparadas por página e identificar duplicatas.
3. Comparar o número de queries antes/depois de comentar temporariamente os `select_related`/`prefetch_related` (em ambiente de desenvolvimento) para confirmar a efetividade da otimização atual.
4. Verificar especificamente se `{{ object_list.count }}` nas listagens gera uma query `COUNT` adicional em relação à contagem já usada pela paginação.
5. Popular o banco com `seed_demo_data` (ou volume maior) antes de medir, para que os resultados sejam representativos.
