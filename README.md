# 🎯 JuriScraper STJ

**Scraper** voltado à extração de ementas do **Superior Tribunal de Justiça (STJ)**. Um script simples, porém poderoso, que visa auxiliar juristas na pesquisa jurisprudencial, salvando em Markdown as ementas extraídas, para facilitar a integração com modelos de Inteligência Artificial Generativa (GenAI). 🤖

<div align="center">
  <img style="max-width: 100%; height: auto;" src="assets/tribunal.jpg" alt="Brasília/DF, 11/09/2024 - Sessão do Pleno, de Emerson Leal" />
  <p><i>Também chamado de "Tribunal da Cidadania", em referência à Constituição Cidadã (CF/88), guardião da <b>legislação federal</b>, ao STJ compete a uniformização e a interpretação desta, além da atuação como instância ordinária e extraordinária em processos das mais diversas naturezas (art. 105, CF/88).</i></p>
</div>

# 🚀 Funcionalidades

- **Extração de Ementas:** 🕸️ Coleta automatizada de ementas do STJ, facilitando a análise de jurisprudência.
- **Formato Markdown:** 📄 Geração de arquivos Markdown, facilitando a integração com modelos de GenAI.
- **Interface Minimalista:** 🎨 Interação através de linha de comando, proporcionando praticidade às buscas.

# ✅ Pré-requisitos

- Python 3.12 ou superior, disponível através do [**site oficial**](https://www.python.org/downloads/).

# 🛠️ Instalação Local

```bash
# Clone o repositório
git clone https://github.com/germanocastanho/juriscraper-stj.git

# Acesse o diretório
cd juriscraper-stj

# Configure um ambiente virtual
python3 -m venv .venv
source .venv/bin/activate

# Instale as dependências
pip install -r requirements.txt

# Execute o script "main.py"
python3 main.py
```

# 📜 Software Livre

Distribuído sob a [Licença GPLv3](LICENSE), garantindo liberdade de uso, modificação e redistribuição do software, desde que preservadas estas liberdades em quaisquer versões derivadas. Utilizando ou contribuindo, você apoia a filosofia de **software livre** e auxilia a construção de um ambiente tecnológico libertário! ✊
