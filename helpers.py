from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver import ChromeOptions as Options

from config import TAGS, ATTRIBUTES_PRIORITY, SHOW_HIDDEN_ELEMENTS


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
            if not SHOW_HIDDEN_ELEMENTS and not is_visible(element):
                continue
            element_result = {}
            xpath = f"//{tag}"
            for attr in ATTRIBUTES_PRIORITY:
                if element.has_attr(attr):
                    value = element[attr]
                    if type(value) is list:
                        value = " ".join(value)
                    xpath += "[@{}='{}']".format(attr, value)
                    break
            element_result["xpath"] = xpath
            element_result["attributes"] = element.attrs
            class_attr = element_result["attributes"].get("class")
            if (class_attr and isinstance(class_attr, list)):
                element_result["attributes"]["class"] = " ".join(class_attr)
            result.append(element_result)
    return result


def get_title(soup: bs):
    title = soup.find("title")
    return title.get_text()

def is_visible(tag):
    # loads the style attribute of the element
    style = tag.attrs.get('style', False)

    # checks if the element is hidden
    if style and ('hidden' in style or 'display: none' in style or 'display:none' in style):
        return False

    # makes a recursive call to check the parent as well
    parent = tag.parent
    if parent and not is_visible(parent):
        return False

    # neither the element nor its parent(s) are hidden, so return True
    return True