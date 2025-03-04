# 🎯 JuriScraper STJ

**Web Scraper** desenvolvido em Python 🐍 especializado na extração de ementas do **Superior Tribunal de Justiça (STJ)** 🏛️. Um script simples, mas podedoso, que auxilia juristas com a automação 🦾 da coleta de precedetes recentes da Corte Superior. Através dele, são coletadas as 10 últimas decisões do Tribunal ⚖️ acerca do tema pesquisado; em seguida, as decisões são salvas em um arquivo Markdown 📜, perfeito para a alimentação de Large Language Models (LLMs)! 🤖

<br />

## 🚀 Sobre o Projeto

- **Interface**: 🎨 Interface amigável via linha de comando;
- **Pesquisa**: 🔍 Pesquisa automatizada no site do Tribunal;
- **Extração**: 📤 Extração eficiente de ementas judiciais;
- **Salvamento**: 📜 Salvamento otimizado para [**GenAIs (RAG)**](https://www.promptingguide.ai/techniques/rag).

<br />

## 🏛️ Sobre o Tribunal

<div align="center">
  <img style="max-width: 100%; height: auto;" src="assets/tribunal.jpg" alt="Brasília/DF, 11/09/2024 - Sessão do Pleno, de Emerson Leal" />
  <p><em>Guardião da <b>legislação federal</b>, ao STJ compete a uniformização e a interpretação desta, além da atuação como instância ordinária e extraordinária em processos das mais diversas naturezas (art. 105, CF/88). Curiosidade! Também é chamado de "Tribunal da Cidadania", em referência à Constituição Cidadã (CF/88).</em></p>
</div>

<br clear="both">

## 📋 Pré-requisitos

- [**Python**](https://www.python.org/) 🐍 para interpretação e eventual modificação do script [`main.py`](https://github.com/germanocastanho/juriscraper-stj/blob/main/main.py);
- [**Pip**](https://pypi.org/project/pip/) 📦 para instalação de dependências, contidas no arquivo [`requirements.txt`](https://github.com/germanocastanho/juriscraper-stj/blob/main/requirements.txt);
- [**Git**](https://git-scm.com/) 🐙 para clonagem do repositório e eventual versionamento de contribuições;
- [**Venv**](https://docs.python.org/3/library/venv.html) 🌍 para criação e gerenciamento de ambientes virtuais (recomendado).

<br />

> _O projeto utiliza o **WebDriver do Chrome** para automação da navegação web. Em versões mais recentes do Chrome, junto deste, aquele vem instalado por padrão. De todo modo, certifique-se de que o WebDriver está instalado e configurado corretamente no seu sistema. Para mais informações, acesse a [documentação oficial](https://www.selenium.dev/documentation/en/webdriver/driver_requirements/)._

> _Visando uma melhor formatação do documento, que por padrão é criado **sem quebras de linha**, recomenda-se a utilização do editor de texto [VS Code](https://code.visualstudio.com/), configurado da seguinte forma - para as configurações do Markdown, acrescente os pares nome/valor: `"editor.wordWrap": "wordWrapColumn"`, `"editor.wordWrapColumn": 80`, e `"editor.rulers": [80]`._

<br clear="both">

## 📚 Bibliotecas

- [**Time**](https://docs.python.org/3/library/time.html) ⏳ para manipulação de atrasos no script;
- [**UUID**](https://docs.python.org/3/library/uuid.html) 🆔 para geração de identificadores únicos;
- [**Pathlib**](https://docs.python.org/3/library/pathlib.html) 📂 para manipulação de arquivos;
- [**BeautifulSoup**](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) 🥣 para parseamento de HTML;
- [**Selenium**](https://www.selenium.dev/documentation/en/) 💻 para automação do navegação web.

<br />

## 📦 Instalação

```bash
# Clone o repositório
git clone https://github.com/germanocastanho/juriscraper-stj.git

# Acesse o diretório
cd juriscraper-stj

# Configure o ambiente virtual
python3 -m venv .venv
source .venv/bin/activate

# Instale as dependências
pip install -r requirements.txt

# Execute o script "main.py"
python3 main.py
```

<br />

## 🤝 Contribuições

Contribuições são sempre bem-vindas! Se deseja colaborar, siga [boas práticas](https://peps.python.org/pep-0008/) em Python e sugira melhorias relevantes. Faça um fork do repositório, implemente suas alterações e envie um pull request. Caso encontre problemas ou tenha sugestões, abra uma [issue](https://github.com/germanocastanho/juriscraper-stj/issues). Juntos, podemos tornar o **JuriScraper** ainda mais incrível! 🚀

<br />

> _**⚠️ OBS**: o projeto baseia-se na **estrutura HTML** do site do STJ em 2025. Em havendo alterações significativas nesta estrutura, o script provavelmente não funcionará de maneira adequada, devendo ser adaptado, o que torna as contribuições ainda mais importantes! Caso isso ocorra, abra uma [issue](https://github.com/germanocastanho/juriscraper-stj/issues) para que possamos corrigir o problema._

<br clear="both">

## 📜 Licença GPL-3.0

Distribuído sob a [**Licença Pública Geral GNU v3.0 (GPL-3.0)**](https://www.gnu.org/licenses/gpl-3.0.html), garantindo liberdade de uso, modificação e redistribuição do software, desde que preservados os mesmos direitos em quaisquer versões derivadas. Ao utilizar ou contribuir com o projeto, você apoia a filosofia de **software livre** e a promoção de um ambiente colaborativo e aberto à inovação! 🔬

<br />

## ✉️ Contato

Quer **colaborar com o projeto** 💻 ou apenas **trocar ideiais?** 📚 Todas as formas de contato e redes sociais estão disponíveis no meu [**Linktr.ee**](https://linktr.ee/germanocastanho)! 🌳 Fico à disposição para discutir Tecnologia, Filosofia, Direito ou qualquer ideia interessante que nos inspire a criar algo novo 🚀. Obrigado por visitar este espaço e por dedicar seu tempo! Saúde, e nos vemos na próxima! 👋

<br />

**Cada linha, um manifesto pela liberdade!** ✊🏴
