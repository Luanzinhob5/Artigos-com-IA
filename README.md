# IA Criadora de Artigos Científicos

Este projeto utiliza Inteligência Artificial para gerar artigos científicos completos a partir de um tema fornecido pelo usuário. O sistema é composto por múltiplos agentes especializados, cada um responsável por uma etapa do processo de pesquisa, análise, resumo e formatação do artigo.

---

## Tecnologias Utilizadas

- **Python**: Linguagem principal do backend.
- **Flask**: Framework web utilizado para criar a interface e conectar o usuário à IA.
- **CrewAI**: Framework para orquestração de múltiplos agentes de IA, permitindo a divisão do trabalho em tarefas especializadas.
- **OpenAI GPT-4**: Modelo de linguagem utilizado para geração e análise de texto.
- **dotenv**: Gerenciamento seguro de variáveis de ambiente (como API keys).
- **HTML & CSS**: Estrutura e estilização da interface web, inspirada no visual do ChatGPT.
- **JavaScript (AJAX)**: Para envio de perguntas e exibição de respostas sem recarregar a página.

---

## Estrutura dos Agentes e Tasks

O sistema é dividido em quatro agentes principais, cada um com sua respectiva task:

### 1. **Agente Pesquisador (`agente_pesquisador`)**
- **Task:** `task_pesquisar`
- **Função:** Realiza uma pesquisa profunda sobre o tema solicitado, buscando informações em fontes científicas confiáveis (arXiv, PubMed, SciELO, etc.) e retorna uma lista detalhada de dados e referências.

### 2. **Agente Analista (`agente_analista`)**
- **Task:** `task_analizar_texto`
- **Função:** Analisa criticamente os dados coletados, elimina duplicidades e destaca os pontos-chave mais relevantes para a redação do artigo científico.

### 3. **Agente Resumidor (`agente_resumo`)**
- **Task:** `task_resumir_texto`
- **Função:** Elabora um resumo técnico e preciso das descobertas, organizando as ideias de forma clara e científica.

### 4. **Agente Formatador (`agente_artigo`)**
- **Task:** `task_formatar_artigo`
- **Função:** Converte o resumo técnico em um artigo científico completo, estruturado conforme normas acadêmicas (ABNT ou APA), incluindo introdução, metodologia, resultados, discussão e conclusão.

---

## Sobre o Projeto

O **IA Criadora de Artigos Científicos** foi desenvolvido para automatizar o processo de produção acadêmica, facilitando a geração de textos científicos de alta qualidade a partir de um simples tema. O usuário interage com uma interface web moderna e responsiva, inspirada no ChatGPT, onde pode enviar o tema desejado e receber o artigo pronto em poucos instantes.

O projeto demonstra como agentes de IA podem colaborar em etapas distintas para entregar resultados complexos e úteis, promovendo inovação na área de automação científica e educacional.

---

## Como rodar o projeto

1. Instale as dependências com `pip install -r requirements.txt`.
2. Configure sua chave da OpenAI em um arquivo `.env`.
3. Execute o servidor Flask com `python app.py`.
4. Acesse `http://localhost:5000` no navegador.

---

**Sinta-se à vontade para contribuir ou adaptar este projeto para suas necessidades acadêmicas!**
