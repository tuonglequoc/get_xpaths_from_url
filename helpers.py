from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver import ChromeOptions as Options


options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--remote-debugging-port=9222")


def get_data_from_url_by_chromedriver(url: str):
    driver = webdriver.Chrome("chromedriver", chrome_options=options)
    driver.get(url)
    content = driver.page_source
    driver.close()
    return content


def get_bs_data(html_text: str):
    return bs(html_text, "html.parser")
