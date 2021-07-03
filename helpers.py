from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver import ChromeOptions as Options


TAGS = ["input", "textarea", "select", "button", "a"]
ATTRIBUTE_LIST = [
    "id",
    "name",
    "placeholder",
    "value",
    "title",
    "type",
    "href",
    "class",
]

options = Options()
options.add_argument("--headless")
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")
# options.add_argument("--remote-debugging-port=9222")


def get_data_from_url_by_chromedriver(url: str):
    driver = webdriver.Chrome("chromedriver", chrome_options=options)
    driver.get(url)
    content = driver.page_source
    driver.close()
    return content


def get_bs_data(html_text: str):
    return bs(html_text, "html.parser")


def get_xpath(soup: bs):
    result = []
    for tag in TAGS:
        elements = soup.find_all(tag)
        for element in elements:
            if element.has_attr("type") and element["type"] == "hidden":
                continue
            element_result = {}
            xpath = f"//{tag}"
            for attr in ATTRIBUTE_LIST:
                if element.has_attr(attr):
                    value = element[attr]
                    if type(value) is list:
                        value = " ".join(value)
                    xpath += "[@{}='{}']".format(attr, value)
                    break
            element_result["xpath"] = xpath
            element_result.update(element.attrs)
            result.append(element_result)
    return result


def get_title(soup: bs):
    title = soup.find("title")
    return title.get_text()
