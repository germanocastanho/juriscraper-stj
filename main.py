# Copyleft 🄯 2025, Germano Castanho
# Free software under the GNU GPL v3


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


def get_user_keywords():
    print("Welcome to JuriScraper STJ! 🎯")
    time.sleep(1)

    keywords = input("What shall we research? 🔍\n")
    return keywords


def access_stj_webpage():
    print("Accessing the Court website... 💻")
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


def search_user_keywords(driver, keywords):
    print("Searching for relevant headnotes... 🔎")
    text_input = driver.find_element(By.ID, "pesquisaLivre")
    text_input.send_keys(keywords)
    text_input.send_keys(Keys.RETURN)
    time.sleep(3)
    return None


def get_max_headnotes_per_page(driver):
    print("Configuring headnotes selection... ⚙️")
    select_box = driver.find_element(By.ID, "qtdDocsPagina")
    options = select_box.find_elements(By.TAG_NAME, "option")
    max_value = max(
        options,
        key=lambda x: int(x.get_attribute("value")),
    )
    max_value.click()
    time.sleep(3)
    return None


# TODO: Format the headnotes properly
def extract_stj_headnotes(driver):
    print("Extracting Court headnotes... 📜")
    soup = BeautifulSoup(driver.page_source, "html.parser")

    sources = []
    index = 1

    while True:
        textarea = soup.find("textarea", {"id": f"textSemformatacao{index}"})
        if not textarea:
            break
        sources.append(textarea.text.strip())
        index += 1

    headnotes = "\n\n".join(sources)
    return headnotes


def save_stj_headnotes(headnotes):
    print('Saving headnotes to "data"... 📥')
    notes_file = HEADNOTES / f"{uuid.uuid4()}.md"
    with open(notes_file, "w", encoding="utf-8") as f:
        f.write(headnotes)

    time.sleep(3)
    return None


def exit_web_browser(driver):
    print("Closing JuriScraper... See you later! 👋")
    driver.quit()
    time.sleep(1)
    return None


def main():
    keywords = get_user_keywords()
    driver = access_stj_webpage()
    search_user_keywords(driver, keywords)
    get_max_headnotes_per_page(driver)
    headnotes = extract_stj_headnotes(driver)
    save_stj_headnotes(headnotes)
    exit_web_browser(driver)
    return None


if __name__ == "__main__":
    main()
