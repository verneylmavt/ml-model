import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

urls = [
    "https://verneylogyt.streamlit.app/",
    "https://verneylogyt-snt-analysis.streamlit.app/",
    "https://verneylogyt-pos-tagging.streamlit.app/",
    "https://verneylogyt-nli.streamlit.app/",
    "https://verneylogyt-ner.streamlit.app/",
    "https://verneylogyt-mov-recsys.streamlit.app/",
    "https://verneylogyt-sn-dgt-recognition.streamlit.app/",
    "https://verneylogyt-nba-vis.streamlit.app/"
    ]

def setup_browser():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def simulate_interaction(driver, url):
    driver.get(url)
    print(f"Loaded: {url}")
    time.sleep(5)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2.5)

    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(2.5)

    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).send_keys('a').send_keys('c').key_up(Keys.CONTROL).perform()
    print("Completed.")

def generate_interactions(driver, urls):
    for url in urls:
        simulate_interaction(driver, url)

if __name__ == "__main__":
    driver = setup_browser()
    try:
        generate_interactions(driver, urls)
    finally:
        driver.quit()
        print("Closed.")
