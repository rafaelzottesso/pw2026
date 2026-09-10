Quero realizar uma engenharia reversa deste projeto Python/Django para produzir uma documentação técnica enxuta, que posteriormente será utilizada como base para um artigo científico de aproximadamente 12 páginas.

Analise o projeto existente no workspace e gere a documentação somente com base nas evidências encontradas no código, banco/configurações e estrutura do projeto. Não invente funcionalidades, requisitos ou regras de negócio. Quando algo não puder ser determinado com segurança, indique como "não identificado" ou "não foi possível inferir".

O objetivo não é documentar 100% do sistema, mas recuperar os principais elementos necessários para compreender sua estrutura, funcionamento e qualidade.

Documentação a gerar

Crie uma pasta docs/ e organize a documentação em Markdown.

1. Visão geral

Documente brevemente:

objetivo geral do sistema;
objetivos específicos;
problema que o sistema resolve;
principais usuários;
principais funcionalidades;
tecnologias utilizadas.
2. Requisitos

Identifique os principais:

requisitos funcionais (RF);
requisitos não funcionais (RNF);
regras de negócio (RN).

Não tente listar tudo. Priorize os requisitos e regras mais importantes e que possam ser sustentados pelo código.

3. UML e arquitetura

Crie os principais diagramas usando Mermaid, diretamente nos arquivos Markdown.

Produza:

diagrama de casos de uso;
diagrama de classes simplificado, focando nas principais entidades/models;
diagrama de sequência de uma funcionalidade importante;
diagrama de arquitetura/componentes do sistema;
diagrama entidade-relacionamento simplificado, se houver informações suficientes.

Os diagramas devem ser legíveis e evitar excesso de elementos. Prefira representar os principais componentes e relacionamentos.

4. Testes

Analise os testes existentes no projeto e documente:

quais tipos de testes existem;
principais funcionalidades testadas;
principais lacunas percebidas;
uma avaliação breve da cobertura/qualidade dos testes, caso seja possível obter essa informação.

Não crie testes automaticamente neste momento.

5. Desempenho

Analise o projeto considerando possíveis problemas de desempenho do Django.

Verifique, quando aplicável:

consultas ao banco;
possíveis problemas de N+1 queries;
uso de select_related/prefetch_related;
consultas repetitivas;
operações potencialmente custosas;
pontos que merecem investigação.

Considere também o uso do Django Debug Toolbar como ferramenta de análise de desempenho. Caso ela já esteja instalada/configurada, documente seu uso e os principais resultados encontrados. Caso não esteja, indique brevemente como ela poderia ser utilizada para validar os pontos identificados.

Não invente métricas de desempenho. Se não houver medição, deixe claro que são pontos de investigação.

6. Rastreabilidade

Crie uma pequena matriz relacionando:

Requisito → Caso de uso → componente/classe → implementação

Inclua somente os principais elementos.

7. Síntese da engenharia reversa

Ao final, faça uma síntese contendo:

principais características arquiteturais encontradas;
principais regras de negócio identificadas;
principais pontos positivos;
principais problemas ou riscos encontrados;
principais lacunas de documentação;
sugestões de melhoria.
Regras importantes
Baseie tudo na análise real do projeto.
Não invente informações.
Seja objetivo e evite documentação excessivamente detalhada.
Priorize os elementos mais relevantes para um artigo científico.
Use Markdown.
Use Mermaid para todos os diagramas.
Mantenha os diagramas simples, legíveis e visualmente organizados.
Sempre que possível, indique no texto de onde a informação foi inferida (por exemplo: model, view, URL, teste, configuração etc.).
Não altere o código da aplicação.
Antes de gerar a documentação, explore a estrutura do projeto e identifique os arquivos mais relevantes.
Ao final, apresente um resumo dos principais achados e dos arquivos analisados.