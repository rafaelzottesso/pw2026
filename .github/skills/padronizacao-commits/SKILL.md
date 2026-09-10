---
name: padronizacao-commits
description: "Padroniza mensagens de commit deste projeto usando Conventional Commits. Use ao criar, revisar ou corrigir mensagens de commit, especialmente antes de executar github.py, git commit ou git push."
argument-hint: "Descreva as mudancas que serao commitadas"
---

# Padronizacao de commits

## Quando usar

- Criar uma mensagem para um conjunto de mudancas.
- Revisar uma mensagem antes de executar `git commit` ou `github.py`.
- Corrigir mensagens inconsistentes no historico do projeto.
- Preparar commits de codigo Django, documentacao, testes, configuracao ou estilos.

## Formato obrigatorio

Use uma linha inicial neste formato:

```text
tipo(escopo): descricao curta no imperativo
```

O escopo e opcional:

```text
tipo: descricao curta no imperativo
```

Regras para a linha inicial:

- Escreva em minusculas.
- Use no maximo 72 caracteres quando possivel.
- Nao termine com ponto.
- Descreva a intencao do commit, nao apenas o arquivo alterado.
- Use verbo no imperativo, por exemplo `adiciona`, `corrige`, `atualiza` ou `remove`.

## Tipos permitidos

- `feat`: adiciona uma funcionalidade para o usuario.
- `fix`: corrige um defeito.
- `docs`: altera documentacao ou artigos.
- `test`: adiciona ou altera testes.
- `refactor`: reorganiza codigo sem mudar o comportamento externo.
- `perf`: melhora desempenho.
- `style`: altera formatacao, CSS ou estilo sem mudar a logica.
- `build`: altera dependencias ou processo de build.
- `ci`: altera automacao de integracao ou entrega continua.
- `chore`: realiza manutencao que nao se encaixa nos tipos anteriores.

## Procedimento

1. Inspecione `git status` e `git diff` para entender todas as mudancas.
2. Separe mudancas de assuntos diferentes; sugira commits independentes quando necessario.
3. Escolha o tipo que representa a mudanca principal e um escopo curto, como `website`, `docs`, `artigo` ou `deploy`.
4. Escreva a linha inicial conforme o formato obrigatorio.
5. Se a mudanca exigir contexto, acrescente um corpo separado por uma linha em branco. Explique o problema e a decisao, sem repetir o diff.
6. Se houver incompatibilidade, acrescente `BREAKING CHANGE:` no rodape e explique o impacto e a migracao.
7. Revise a mensagem contra as regras desta skill antes de usa-la no `github.py` ou no Git.

## Exemplos

```text
feat(website): adiciona listagem de campeonatos
fix(website): corrige paginacao de jogadores
docs: atualiza rastreabilidade dos requisitos
test(website): cobre cadastro de modalidades
refactor(website): extrai filtro de campeonatos
style: ajusta layout responsivo da pagina inicial
chore: atualiza dependencias do projeto
```

Exemplo com corpo:

```text
fix(website): corrige filtro por campus

Mantem os parametros da busca durante a paginacao para evitar que o
resultado volte a exibir todos os campi.
```

Exemplo de incompatibilidade:

```text
refactor(website)!: renomeia campo publico de jogador

BREAKING CHANGE: consumidores devem usar `nome_completo` no lugar de
`nome`. Atualize formularios e integracoes antes do proximo deploy.
```

## Checklist final

- A mensagem explica uma unica mudanca coerente.
- O tipo corresponde ao efeito da mudanca.
- O escopo e curto e reconhecivel no projeto.
- A descricao esta no imperativo, em minusculas e sem ponto final.
- Nao ha referencias a credenciais, tokens ou dados locais.
- Nao use `git add *`, `git commit` ou `git push` sem autorizacao explicita para executar a operacao.