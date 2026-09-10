Quero escrever um artigo científico de aproximadamente 12 páginas, para um evento local da área de Informática, com base na engenharia reversa realizada em um projeto real desenvolvido em Python/Django.

No workspace existe um arquivo chamado formato.latex, que contém a estrutura/template básica exigida pelo evento. Também existe uma pasta docs/, contendo a documentação e os resultados obtidos durante a engenharia reversa do sistema.

Sua tarefa é produzir o artigo científico completo em LaTeX, utilizando o formato.latex como base e as informações existentes em docs/.

Objetivo do artigo

O artigo deve apresentar a aplicação de engenharia reversa em um sistema Django que não possuía documentação formal, mostrando como informações do código-fonte foram utilizadas para recuperar:

requisitos;
regras de negócio;
arquitetura;
modelos UML;
modelo de dados;
testes;
aspectos de desempenho.

O trabalho deve ser apresentado como um estudo de caso, e não simplesmente como uma documentação do sistema.

A ideia central é:

Sistema sem documentação → análise do software → recuperação de informações → modelagem/documentação → análise de testes e desempenho → identificação de resultados, limitações e oportunidades de melhoria.

Estrutura do artigo

Organize o artigo aproximadamente nas seguintes seções:

1. Introdução

Apresente:

contexto;
problema da ausência de documentação em sistemas de software;
importância da engenharia reversa;
motivação do trabalho;
problema de pesquisa;
objetivo geral;
objetivos específicos;
contribuição do trabalho.

Utilize como questão de pesquisa, caso seja adequada aos resultados:

Como a engenharia reversa pode auxiliar na recuperação da documentação arquitetural e funcional de um sistema web desenvolvido em Django que não possui documentação formal?

Não transforme a introdução em uma descrição detalhada do sistema.

2. Fundamentação teórica

Apresente de forma objetiva os conceitos necessários para compreender o trabalho:

2.1 Engenharia reversa de software
2.2 Documentação e arquitetura de software
2.3 UML e modelagem de software
2.4 Django e ferramentas de análise

Inclua referências acadêmicas e técnicas relevantes.

Priorize fontes científicas, livros, documentação oficial e trabalhos relacionados.

Não invente referências.

3. Materiais e métodos

Explique como a engenharia reversa foi realizada.

Descreva:

o sistema analisado;
tecnologias utilizadas;
artefatos analisados;
análise do código;
identificação dos requisitos;
identificação das regras de negócio;
recuperação da arquitetura;
geração dos diagramas;
análise dos testes;
análise de desempenho;
forma de consolidação dos resultados.

Apresente o processo de forma resumida, podendo utilizar uma figura ou fluxograma.

Uma representação conceitual pode ser:

Análise do código → Extração de evidências → Inferência dos requisitos e regras → Modelagem → Testes → Análise de desempenho → Documentação.

Deixe claro que a documentação foi recuperada a partir de evidências do sistema existente.

4. Estudo de caso

Caracterize brevemente o sistema analisado.

Apresente apenas informações relevantes:

finalidade;
principais funcionalidades;
arquitetura;
tecnologias;
aplicações/módulos Django;
banco de dados;
características relevantes.

Utilize informações reais encontradas na documentação de engenharia reversa.

Não exponha informações sensíveis.

5. Resultados

Esta deve ser a principal seção do artigo.

5.1 Requisitos e regras de negócio

Apresente uma seleção dos principais requisitos funcionais, requisitos não funcionais e regras de negócio recuperados.

Não coloque uma lista enorme.

Priorize os elementos mais representativos.

Utilize tabelas quando forem mais eficientes que texto.

5.2 Modelagem UML

Apresente os principais diagramas recuperados:

caso de uso;
classes;
sequência.

Utilize os diagramas já produzidos na documentação.

Se os diagramas estiverem em Mermaid e o template LaTeX não permitir sua inclusão diretamente, converta-os para um formato adequado para o artigo, como PDF, SVG ou PNG, preservando sua qualidade visual.

Não redesenhe os diagramas de maneira conceitualmente diferente do que foi recuperado.

5.3 Arquitetura e modelo de dados

Apresente:

arquitetura geral;
principais componentes;
modelo de dados/DER.

Utilize figuras simplificadas e legíveis.

5.4 Testes

Apresente os resultados da análise dos testes existentes.

Discuta:

tipos de testes encontrados;
funcionalidades cobertas;
resultados obtidos;
principais lacunas.

Utilize números reais obtidos na análise.

Não invente cobertura ou resultados.

5.5 Análise de desempenho

Apresente a análise realizada com base no Django Debug Toolbar, quando disponível.

Discuta:

quantidade de consultas;
tempo de execução;
consultas repetitivas;
possíveis problemas de N+1;
uso de select_related e prefetch_related;
outros pontos relevantes encontrados.

Utilize somente métricas efetivamente medidas.

Caso não existam métricas experimentais, deixe isso explícito e apresente a análise como inspeção ou diagnóstico preliminar.

6. Discussão

Interprete os resultados.

Não apenas repita o que foi apresentado na seção anterior.

Discuta:

quais informações foram facilmente recuperadas;
quais foram difíceis de recuperar;
quais regras de negócio estavam implícitas no código;
como a arquitetura pôde ser reconstruída;
o que os testes revelaram;
o que a análise de desempenho revelou;
quais benefícios a engenharia reversa trouxe;
limitações da abordagem.

Relacione os resultados com a fundamentação teórica e, quando possível, com trabalhos relacionados.

7. Conclusão

Retome:

objetivo;
principais resultados;
contribuição do trabalho;
limitações;
possíveis trabalhos futuros.

Não introduza resultados novos na conclusão.

Trabalhos relacionados

Caso o template ou o espaço disponível permita, inclua uma subseção de trabalhos relacionados dentro da fundamentação teórica ou antes da metodologia.

Procure trabalhos científicos relacionados a:

engenharia reversa;
recuperação de arquitetura;
documentação automática;
documentação de sistemas legados;
análise estática de software;
engenharia reversa em aplicações web;
manutenção de software.

Não invente trabalhos ou citações.

Referências

Utilize referências reais e relevantes.

Priorize:

artigos científicos;
livros acadêmicos;
conferências;
periódicos;
documentação oficial de tecnologias quando apropriado.

Não crie referências fictícias.

Se o formato.latex utilizar BibTeX ou BibLaTeX, mantenha o mecanismo utilizado pelo template.

Uso do formato.latex

O arquivo formato.latex é o template oficial do artigo.

Antes de escrever o artigo:

leia o arquivo;
identifique a classe do documento;
identifique os pacotes utilizados;
identifique o formato de título, autores, seções, figuras, tabelas e referências;
preserve a estrutura exigida pelo template.

Não substitua o template por outro modelo.

Não altere desnecessariamente:

classe do documento;
margens;
fontes;
cabeçalhos;
rodapés;
formatação das referências;
comandos fornecidos pelo evento.

Preencha o template com o conteúdo do artigo.

Uso da documentação existente

Utilize os arquivos em docs/ como fonte principal dos resultados.

Antes de escrever:

leia a documentação produzida;
identifique os principais resultados;
verifique a consistência entre os documentos;
selecione somente o que é relevante para um artigo de 12 páginas.

Não copie a documentação literalmente.

Transforme-a em texto científico, sintetizando os resultados.

Estilo de escrita

O artigo deve:

utilizar linguagem acadêmica;
ser objetivo;
evitar linguagem excessivamente informal;
evitar afirmações sem evidência;
diferenciar fatos observados de inferências;
apresentar resultados antes de interpretá-los;
evitar excesso de detalhes de implementação;
manter foco em engenharia de software.

Não escrever como manual de usuário.

Não escrever como documentação técnica.

O artigo deve apresentar metodologia, resultados e discussão.

Limite de extensão

O artigo deve ser planejado para aproximadamente 12 páginas, considerando o template do evento.

Priorize:

resultados;
metodologia;
fundamentação necessária;
discussão.

Evite gastar muitas páginas descrevendo o funcionamento básico do Django.

Não tente incluir todos os diagramas ou todos os requisitos encontrados.

Selecione os artefatos mais relevantes.

Figuras e tabelas

Priorize figuras e tabelas que contribuam diretamente para o argumento científico.

Sugestão de figuras:

processo de engenharia reversa;
arquitetura do sistema;
diagrama de casos de uso;
diagrama de classes;
diagrama de sequência;
eventualmente DER.

Sugestão de tabelas:

principais requisitos;
principais regras de negócio;
resultados dos testes;
resultados de desempenho;
matriz de rastreabilidade, se houver espaço.

Não sobrecarregue o artigo com figuras.

Validação final

Antes de finalizar o artigo, faça uma revisão verificando:

todas as informações são compatíveis com docs/;
nenhuma métrica foi inventada;
nenhum requisito foi inventado;
os diagramas correspondem ao sistema real;
os resultados apresentados realmente foram obtidos;
as conclusões são sustentadas pelos resultados;
referências são reais;
todas as citações utilizadas aparecem nas referências;
todas as referências citadas são utilizadas no texto;
o documento segue o formato.latex;
o código LaTeX está compilável.

Se houver inconsistência entre documentos, priorize as evidências mais diretamente relacionadas ao código-fonte e sinalize a inconsistência.

Resultado esperado

Gere:

artigo.tex

utilizando formato.latex como base.

Se necessário, crie também uma pasta:

figuras/

para armazenar as figuras utilizadas no artigo.

Ao final, informe brevemente:

quantidade de páginas aproximada;
quantidade de figuras;
quantidade de tabelas;
quantidade de referências;
principais resultados apresentados;
eventuais informações que não puderam ser determinadas.