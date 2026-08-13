# Arena eSports

Sistema Django para gerenciamento de campeonatos de eSports, modalidades, campi, jogadores, inscrições e jogos.

## Requisitos

- Python 3.12
- PostgreSQL acessível pela aplicação
- Ambiente virtual Python recomendado

As dependências do projeto estão em `requirements.txt`. Entre as principais estão Django 5.2, django-braces, crispy-forms, django-filter e Django Debug Toolbar.

## Instalação

No Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Se a política do PowerShell impedir a ativação do ambiente, execute os comandos usando diretamente `.venv\Scripts\python.exe`.

## Configuração do banco

O projeto usa PostgreSQL configurado em `pw2026/settings.py`. Antes de executar a aplicação:

1. Configure a URL de conexão do PostgreSQL em uma variável de ambiente ou na configuração local.
2. Nunca publique usuário, senha ou URL de conexão no GitHub, no README ou em mensagens.
3. Em caso de troca de banco, aplique as migrações antes de iniciar a aplicação.

Comandos:

```powershell
.\.venv\Scripts\python.exe manage.py makemigrations
.\.venv\Scripts\python.exe manage.py migrate
```

## Execução local

```powershell
.\.venv\Scripts\python.exe manage.py runserver
```

Acesse:

- Aplicação: `http://127.0.0.1:8000/`
- Admin: `http://127.0.0.1:8000/admin/`
- Debug Toolbar: aparece nas páginas quando acessadas pelo IP local permitido.

Para criar um administrador:

```powershell
.\.venv\Scripts\python.exe manage.py createsuperuser
```

## Dados de demonstração

O comando `seed_demo_data` cria dados fictícios e pode ser executado novamente sem duplicar os registros:

```powershell
.\.venv\Scripts\python.exe manage.py seed_demo_data
```

O comando cria ou atualiza:

- Campi, modalidades e fases-base
- Usuários fictícios
- Jogadores vinculados aos usuários
- Campeonatos e modalidades relacionadas
- Inscrições, jogadores das equipes e responsáveis
- Jogos com fases, resultados e vencedores

Os usuários fictícios novos recebem inicialmente a senha de demonstração `Arena@2026`. Altere essas senhas em ambientes compartilhados ou de produção.

A população é executada dentro de uma transação e usa chaves naturais estáveis, permitindo repopular um banco novo ou atualizar os dados de demonstração sem criar duplicatas.

## Autenticação

Rotas principais:

- `/login/`: login usando o template compartilhado `website/form.html`
- `/logout/`: logout
- `/alterar-senha/`: alteração de senha para usuários autenticados

As views protegidas usam `LoginRequiredMixin`. Operações de modalidade usam `GroupRequiredMixin` conforme os grupos definidos no projeto:

- Cadastro e edição: `Administrador` ou `Organizador`
- Exclusão: `Administrador`

O menu principal usa `request.user.is_authenticated` para exibir opções adequadas a usuários autenticados e visitantes.

## Funcionalidades principais

- Listagens paginadas com `paginate_by`
- Paginação reutilizável em `website/templates/website/includes/pagination.html`
- Preservação dos filtros de busca nos links de paginação por meio da templatetag `query_transform`
- ListViews para modalidades, fases, jogadores, campeonatos, campi, inscrições e jogos
- Tela `Meus Jogos`, filtrada pelos jogadores associados ao usuário autenticado
- Templates de detalhe para os modelos principais
- Formulários baseados em `CreateView`, `UpdateView` e `DeleteView`

## Otimização de consultas

As views usam:

- `select_related` para relacionamentos `ForeignKey` e `OneToOneField`
- `prefetch_related` para relacionamentos `ManyToManyField`
- `Q()` e `distinct()` na consulta de `MeusJogos`

As principais relações otimizadas estão em `website/views.py`, incluindo campus de jogadores e campeonatos, campeonato e modalidade de inscrições, e times, fase e modalidade de jogos.

## Django Debug Toolbar

A ferramenta está instalada em `requirements.txt`, registrada em `INSTALLED_APPS`, adicionada ao middleware e disponível pela rota `__debug__/`.

Ela está configurada para funcionar somente em `127.0.0.1`. Use-a durante o desenvolvimento para identificar consultas repetidas e validar o efeito de `select_related` e `prefetch_related`.

Não habilite o Debug Toolbar para acesso público ou produção.

## Testes e verificações

Verificar a configuração Django:

```powershell
.\.venv\Scripts\python.exe manage.py check
```

Executar os testes da aplicação:

```powershell
.\.venv\Scripts\python.exe manage.py test website
```

## Estrutura principal

```text
manage.py                 Comandos administrativos do Django
pw2026/                   Configuração, URLs e WSGI/ASGI do projeto
website/                  Aplicação principal
website/models.py         Modelos do domínio
website/views.py          Views e regras de acesso
website/urls.py           Rotas da aplicação
website/templates/       Templates HTML
website/templatetags/     Tags e filtros de template
website/management/       Comandos administrativos, incluindo o seed
static/                   Arquivos estáticos de desenvolvimento
static_gcloud/            Arquivos coletados para deploy
app.yaml                  Configuração do Google App Engine
requirements.txt          Dependências Python
```

## Deploy no Google App Engine

O projeto possui configuração em `app.yaml` para Python 3.12 e Gunicorn. Antes do deploy:

1. Configure as variáveis e credenciais do banco no ambiente de produção.
2. Não use credenciais embutidas no código-fonte.
3. Execute as migrações no banco de produção.
4. Colete os arquivos estáticos:

```powershell
.\.venv\Scripts\python.exe manage.py collectstatic
```

5. Revise `DEBUG`, `ALLOWED_HOSTS`, dados de autenticação e acesso ao banco antes de publicar.
