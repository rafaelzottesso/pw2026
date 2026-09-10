# 3. UML e Arquitetura

Todos os diagramas abaixo foram reconstruídos a partir do código-fonte (`website/models.py`, `website/views.py`, `website/urls.py`, `pw2026/settings.py`). Foram simplificados para priorizar legibilidade.

## 3.1 Diagrama de Casos de Uso

Baseado nas classes de view em [website/views.py](../website/views.py) e nas restrições de acesso (`LoginRequiredMixin`, `GroupRequiredMixin`).

```mermaid
flowchart LR
    Visitante((Visitante))
    Usuario((Usuário autenticado))
    Organizador((Organizador / Administrador))

    subgraph Sistema["Arena eSports"]
        UC1[Consultar página inicial]
        UC2[Ver detalhes públicos<br/>Campus, Fase, Campeonato,<br/>Inscrição, Jogo]
        UC3[Autenticar-se]
        UC4[Gerenciar Campus/Fase/<br/>Jogador/Campeonato/<br/>Inscrição/Jogo]
        UC5[Ver Meus Jogos]
        UC6[Alterar própria senha]
        UC7[Gerenciar Modalidades]
        UC8[Excluir Modalidades]
    end

    Visitante --> UC1
    Visitante --> UC2
    Visitante --> UC3

    Usuario --> UC1
    Usuario --> UC2
    Usuario --> UC4
    Usuario --> UC5
    Usuario --> UC6

    Organizador --> UC7
    Organizador --> UC8
    Organizador --> UC4
```

Observação: `UC4` agrega os CRUDs de Campus, Fase, Jogador, Campeonato, Inscrição e Jogo porque compartilham o mesmo padrão de acesso (`LoginRequiredMixin`, com filtro adicional por "dono" do registro em Jogador/Campeonato/Inscrição/Jogo — ver seção de Regras de Negócio).

## 3.2 Diagrama de Classes (modelo de domínio simplificado)

Baseado em [website/models.py](../website/models.py) e nas migrações [0001_initial.py](../website/migrations/0001_initial.py) e [0002_...py](../website/migrations/0002_campus_campeonato_campus_alter_jogador_campus_and_more.py).

```mermaid
classDiagram
    class User {
        <<django.contrib.auth>>
        +username
        +email
        +is_staff
    }

    class Campus {
        +nome: CharField
    }

    class Modalidade {
        +nome: CharField
    }

    class Fase {
        +nome: CharField
        +quantidade_jogos: PositiveSmallInteger
        +sequencia: PositiveSmallInteger
    }

    class Jogador {
        +nome: CharField
        +telefone: CharField
        +cadastrado_em: DateTime
        +atualizado_em: DateTime
    }

    class Campeonato {
        +nome: CharField
        +categoria: CharField
        +data_inicio: DateTime
        +data_limite_inscricao: DateTime
        +cadastrado_em: DateTime
        +atualizado_em: DateTime
    }

    class Inscricao {
        +nome_time: CharField
        +confirmada: Boolean
        +confirmada_em: DateTime
        +inscrito_em: DateTime
    }

    class Jogo {
        +data_hora: DateTime
        +resultado: CharField
        +cadastrado_em: DateTime
        +atualizado_em: DateTime
    }

    Jogador "1" --> "1" User : usuario (OneToOne)
    Jogador "N" --> "1" Campus : campus (PROTECT)

    Campeonato "N" --> "1" Campus : campus (PROTECT)
    Campeonato "N" --> "1" User : cadastrado_por (PROTECT)
    Campeonato "N" --> "N" Modalidade : modalidades (M2M)

    Inscricao "N" --> "1" Campeonato : campeonato (PROTECT)
    Inscricao "N" --> "1" Modalidade : modalidade (PROTECT)
    Inscricao "N" --> "1" User : inscrito_por (PROTECT)
    Inscricao "N" --> "N" Jogador : jogadores (M2M)

    Jogo "N" --> "1" Inscricao : time_1 (PROTECT)
    Jogo "N" --> "1" Inscricao : time_2 (PROTECT)
    Jogo "0..1" --> "1" Inscricao : vencedor (PROTECT, opcional)
    Jogo "N" --> "1" Fase : etapa (PROTECT)
    Jogo "N" --> "1" Modalidade : modalidade (PROTECT)
    Jogo "N" --> "1" User : cadastrado_por (PROTECT)
```

## 3.3 Diagrama de Sequência — Cadastro de Inscrição

Fluxo reconstruído a partir de `InscricaoCreate` em [website/views.py](../website/views.py), do template [form.html](../website/templates/website/form.html) e das URLs em [website/urls.py](../website/urls.py).

```mermaid
sequenceDiagram
    actor U as Usuário autenticado
    participant N as Navegador
    participant D as Django URL Dispatcher
    participant V as InscricaoCreate (View)
    participant F as ModelForm (Inscricao)
    participant M as Model Inscricao (ORM)
    participant BD as PostgreSQL

    U->>N: Acessa "Nova Inscrição"
    N->>D: GET /cadastrar/inscricao/
    D->>V: roteia para InscricaoCreate
    V-->>N: renderiza form.html (crispy-forms)
    U->>N: Preenche e envia formulário
    N->>D: POST /cadastrar/inscricao/ (+ csrf_token)
    D->>V: roteia para InscricaoCreate.post()
    V->>F: valida dados do formulário
    alt formulário inválido
        F-->>V: erros de validação
        V-->>N: reexibe form.html com erros
    else formulário válido
        V->>V: form_valid(form): define inscrito_por = request.user
        V->>M: salva instância (form.save)
        M->>BD: INSERT INTO website_inscricao (...)
        BD-->>M: registro criado
        V->>V: messages.success("... cadastrada com sucesso!")
        V-->>N: HTTP 302 redirect para inscricao_list
        N->>D: GET /listar/inscricoes/
        D-->>N: renderiza lista + toast de sucesso
    end
```

## 3.4 Diagrama de Arquitetura / Componentes

Baseado em [pw2026/settings.py](../pw2026/settings.py), [app.yaml](../app.yaml) e na estrutura de pastas do repositório.

```mermaid
flowchart TB
    subgraph Cliente
        Browser["Navegador (Bootstrap 5 + JS)"]
    end

    subgraph GAE["Google App Engine (produção)"]
        Gunicorn["Gunicorn\n(1 worker, 6 threads)"]
    end

    subgraph Django["Aplicação Django (pw2026)"]
        URLs["pw2026/urls.py\nwebsite/urls.py"]
        Views["website/views.py\n(Class-Based Views)"]
        Forms["Forms\n(django-crispy-forms)"]
        Models["website/models.py\n(ORM)"]
        Templates["website/templates/\n(Django Templates)"]
        Admin["Django Admin\n(website/admin.py)"]
        Messages["django.contrib.messages"]
        Auth["django.contrib.auth\n+ django-braces"]
        DebugToolbar["django-debug-toolbar\n(apenas 127.0.0.1)"]
        SeedCmd["management/commands/\nseed_demo_data.py"]
    end

    subgraph Dados
        PG[("PostgreSQL")]
        Static["Arquivos estáticos\nstatic/ e static_gcloud/"]
    end

    Browser -->|HTTP/HTTPS| Gunicorn
    Browser -->|dev: runserver| URLs
    Gunicorn --> URLs
    URLs --> Views
    Views --> Forms
    Views --> Models
    Views --> Templates
    Views --> Messages
    Views --> Auth
    Models --> PG
    Admin --> Models
    SeedCmd --> Models
    Templates --> Static
    DebugToolbar -.-> Views
    DebugToolbar -.-> Models
```

## 3.5 Diagrama Entidade-Relacionamento (simplificado)

Baseado nas migrações do app `website` e nos campos de `website/models.py`.

```mermaid
erDiagram
    USER ||--o| JOGADOR : "possui"
    CAMPUS ||--o{ JOGADOR : "localiza"
    CAMPUS ||--o{ CAMPEONATO : "sedia"
    USER ||--o{ CAMPEONATO : "cadastra"
    MODALIDADE }o--o{ CAMPEONATO : "compoe"
    CAMPEONATO ||--o{ INSCRICAO : "recebe"
    MODALIDADE ||--o{ INSCRICAO : "classifica"
    USER ||--o{ INSCRICAO : "inscreve"
    JOGADOR }o--o{ INSCRICAO : "integra"
    INSCRICAO ||--o{ JOGO : "disputa_como_time_1"
    INSCRICAO ||--o{ JOGO : "disputa_como_time_2"
    INSCRICAO ||--o{ JOGO : "vence_(opcional)"
    FASE ||--o{ JOGO : "etapa_de"
    MODALIDADE ||--o{ JOGO : "modalidade_de"
    USER ||--o{ JOGO : "cadastra"

    USER {
        int id PK
        string username
        string email
    }
    CAMPUS {
        int id PK
        string nome
    }
    MODALIDADE {
        int id PK
        string nome
    }
    FASE {
        int id PK
        string nome
        int quantidade_jogos
        int sequencia
    }
    JOGADOR {
        int id PK
        string nome
        string telefone
        int campus_id FK
        int usuario_id FK
    }
    CAMPEONATO {
        int id PK
        string nome
        string categoria
        datetime data_inicio
        datetime data_limite_inscricao
        int campus_id FK
        int cadastrado_por_id FK
    }
    INSCRICAO {
        int id PK
        string nome_time
        bool confirmada
        datetime confirmada_em
        int campeonato_id FK
        int modalidade_id FK
        int inscrito_por_id FK
    }
    JOGO {
        int id PK
        datetime data_hora
        string resultado
        int time_1_id FK
        int time_2_id FK
        int vencedor_id FK
        int etapa_id FK
        int modalidade_id FK
        int cadastrado_por_id FK
    }
```
