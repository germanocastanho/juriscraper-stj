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

    driver = webdriver.Chrome(options=opcoes)
    driver.get("https://scon.stj.jus.br/SCON/")
    time.sleep(3)
    return driver


def visitar_pagina(driver, keywords):
    print("Visitando página... 💻")
    input_texto = driver.find_element(By.ID, "pesquisaLivre")
    input_texto.send_keys(keywords)
    input_texto.send_keys(Keys.RETURN)
    time.sleep(3)
    return None


def extrair_ementas(driver):
    print("Extraindo ementas... 📜")
    page_fonte = driver.page_source
    soup = BeautifulSoup(page_fonte, "html.parser")
    titulos = soup.find_all("div", class_="docTitulo")
    textos = soup.find_all("div", class_="docTexto")

    list_ementas = []
    for titulo, texto in zip(titulos, textos):
        chave, valor = titulo.text, texto.text
        dict_ementas = {chave: valor}
        if "Ementa" in dict_ementas:
            list_ementas.append(dict_ementas["Ementa"])
    ementas = "".join(list_ementas)
    time.sleep(3)
    return ementas


def salvar_ementas(ementas):
    print("Salvando ementas... 📥")
    arquivo = ARQUIVOS / f"{uuid.uuid4().hex}.md"
    with open(arquivo, "w", encoding="utf-8") as f:
        f.write(ementas)
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
    ementas = extrair_ementas(driver)
    arquivo = salvar_ementas(ementas)
    finalizar_programa(driver)
    return None


if __name__ == "__main__":
    main()
