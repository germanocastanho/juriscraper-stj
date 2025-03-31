# Copyleft 🄯 2025, Germano Castanho;
# Software livre licenciado sob a GPL-3.0;
# Cada linha, um manifesto pela liberdade!


import time
import uuid
from pathlib import Path

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

HEADNOTES = Path(__file__).parent / "data"
HEADNOTES.mkdir(exist_ok=True)


def interact_user():
    print("Bem-vindo ao JuriScraper STJ! 🎯")
    time.sleep(3)
    keywords = input("O que iremos pesquisar hoje? 🔍\n")
    return keywords


def start_browser():
    print("Iniciando navegador Chrome... 🚀")
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-extensions")
    options.add_argument("--user-agent=Chrome/134.0")
    options.add_argument("--log-level=3")

    driver = webdriver.Chrome(options=options)
    driver.get("https://scon.stj.jus.br/SCON/")
    time.sleep(3)
    return driver


def access_page(driver, keywords):
    print("Acessando site do Tribunal... 💻")
    text_input = driver.find_element(By.ID, "pesquisaLivre")
    text_input.send_keys(keywords)
    text_input.send_keys(Keys.RETURN)
    time.sleep(3)
    return None


# TODO: Adicionar títulos às ementas
def extract_headnotes(driver):
    print("Extraindo ementas do site... 📜")
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, "html.parser")
    titles = soup.find_all("div", class_="docTitulo")
    texts = soup.find_all("div", class_="docTexto")

    notes_list = []
    for title, text in zip(titles, texts):
        key, value = title.text, text.text
        notes_dict = {key: value}
        if "Ementa" in notes_dict:
            notes_list.append(notes_dict["Ementa"])

    headnotes = "".join(notes_list)
    time.sleep(3)
    return headnotes


def save_headnotes(headnotes):
    print("Salvando ementas em 'data/'... 📥")
    notes_file = HEADNOTES / f"{uuid.uuid4()}.md"
    with open(notes_file, "w", encoding="utf-8") as f:
        f.write(headnotes)

    time.sleep(3)
    return None


def exit_browser(driver):
    print("Fechando programa... Até mais! 👋")
    driver.quit()
    time.sleep(3)
    return None


def main():
    keywords = interact_user()
    driver = start_browser()
    access_page(driver, keywords)
    headnotes = extract_headnotes(driver)
    save_headnotes(headnotes)
    exit_browser(driver)
    return None


if __name__ == "__main__":
    main()
