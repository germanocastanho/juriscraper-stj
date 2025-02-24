# Copyleft 🄯, Germano Castanho, 2025;
# Software livre licenciado sob a GPL-3.0;
# Cada linha, um manifesto pela liberdade!


import time
import uuid
from pathlib import Path

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

ARQUIVOS = Path(__file__).parent / "arquivos"
ARQUIVOS.mkdir(exist_ok=True)


def interagir_usuario():
    keywords = input("O que deseja buscar? 🔍\n")
    return keywords.lower()


def iniciar_navegador():
    print("\nIniciando navegador... 🚀")
    opcoes = Options()
    opcoes.add_argument("--headless")
    opcoes.add_argument("--disable-gpu")
    opcoes.add_argument("--window-size=1920x1080")
    opcoes.add_argument("--no-sandbox")
    opcoes.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=opcoes)
    driver.get("https://processo.stj.jus.br/SCON/")
    time.sleep(3)
    return driver


def visitar_pagina(driver, keywords):
    print("Visitando página... 💻")
    input_texto = driver.find_element(By.ID, "pesquisaLivre")
    input_texto.send_keys(keywords)
    input_texto.send_keys(Keys.RETURN)
    time.sleep(3)
    return None


def configurar_pagina(driver):
    print("Configurando página... 🔧")
    select_box = driver.find_element(By.ID, "qtdDocsPagina")
    ActionChains(driver).click(select_box).perform()
    select_box.send_keys(Keys.DOWN)
    select_box.send_keys(Keys.DOWN)
    select_box.send_keys(Keys.RETURN)
    time.sleep(3)
    return None


def extrair_julgados(driver):
    print("Extraindo julgados... 📜")
    page_fonte = driver.page_source
    soup = BeautifulSoup(page_fonte, "html.parser")
    titulos = soup.find_all("div", class_="docTitulo")
    textos = soup.find_all("div", class_="docTexto")

    list_julgados = []
    for titulo, texto in zip(titulos, textos):
        chave, valor = titulo.text, texto.text
        dict_julgados = {chave: valor}
        if "Ementa" in dict_julgados:
            list_julgados.append(dict_julgados["Ementa"])
    julgados = "".join(list_julgados)
    time.sleep(3)
    return julgados


def salvar_julgados(julgados):
    print("Salvando julgados... 📥")
    for legado in ARQUIVOS.glob("*"):
        legado.unlink()
    arquivo = ARQUIVOS / f"{uuid.uuid4().hex}.md"
    with open(arquivo, "w", encoding="utf-8") as f:
        f.write(julgados)
    time.sleep(3)
    return None


def finalizar_programa(driver):
    print("\nFinalizando programa... 👋")
    driver.quit()
    time.sleep(3)
    return None


def main():
    keywords = interagir_usuario()
    driver = iniciar_navegador()
    visitar_pagina(driver, keywords)
    configurar_pagina(driver)
    julgados = extrair_julgados(driver)
    arquivo = salvar_julgados(julgados)
    finalizar_programa(driver)
    return None


if __name__ == "__main__":
    main()
