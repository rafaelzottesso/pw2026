# 4. Testes

## 4.1 Testes existentes

O arquivo [website/tests.py](../website/tests.py) contém apenas o boilerplate padrão gerado pelo Django:

```python
from django.test import TestCase

# Create your tests here.
```

Não há nenhuma classe de teste, caso de teste ou asserção implementada. A execução de `python manage.py test website` confirma essa ausência, retornando:

```
Found 0 test(s).
System check identified no issues (0 silenced).

----------------------------------------------------------------------
Ran 0 tests in 0.000s

NO TESTS RAN
```

Não foram encontrados outros diretórios ou arquivos de teste (`tests/`, `test_*.py`, `conftest.py`, configuração de `pytest`) em nenhum outro ponto do repositório.

## 4.2 Tipos de teste presentes

**Nenhum.** Não há testes unitários, de integração, funcionais/end-to-end ou de API no projeto.

## 4.3 Funcionalidades testadas

**Nenhuma.** Como não existem testes implementados, não há cobertura de nenhuma funcionalidade (models, views, formulários, regras de acesso por grupo, regras de "dono do registro", comando `seed_demo_data`, templates ou URLs).

## 4.4 Principais lacunas percebidas

Com base na criticidade das regras identificadas na seção de [Requisitos](02-requisitos.md), as lacunas mais relevantes para priorização futura seriam:

- Regras de "dono do registro" (RN01–RN04): não há teste que confirme que um usuário não consegue editar/excluir registros de outro usuário (`Jogador`, `Campeonato`, `Inscrição`, `Jogo`).
- Controle de acesso por grupo (RN05): não há teste que confirme que apenas `Administrador`/`Organizador` conseguem operar sobre `Modalidade`.
- Integridade referencial via `PROTECT` (RN06): não há teste validando que a exclusão de um registro referenciado é de fato bloqueada.
- Mensagens de sucesso (RF10) e o `SuccessMessageDeleteMixin` customizado: não há teste unitário para essa classe criada especificamente no projeto.
- View `MeusJogos` (RF08): a consulta com `Q()` e `distinct()` é uma lógica de filtragem não trivial e não possui teste automatizado.
- Comando `seed_demo_data`: não há teste garantindo o comportamento idempotente (`get_or_create`/`update_or_create`) descrito no [README.md](../README.md).
- Autenticação e redirecionamento (`LOGIN_URL`, `LOGIN_REDIRECT_URL`): não há teste validando o fluxo de login/logout.

## 4.5 Avaliação da cobertura/qualidade

Cobertura de testes automatizados: **0%** (nenhum teste executável além do arquivo padrão vazio). Não há ferramenta de cobertura (`coverage.py`, `pytest-cov`) configurada no `requirements.txt`, portanto não foi possível medir cobertura de linha/branch — a afirmação acima decorre diretamente da ausência de testes, não de uma métrica calculada.

Este é o achado mais crítico da análise de qualidade: qualquer alteração futura no código (incluindo os models com `on_delete=PROTECT`, as regras de propriedade dos registros e o controle de acesso por grupo) não possui uma rede de segurança automatizada.
