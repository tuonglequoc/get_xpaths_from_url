from fastapi import FastAPI
from fastapi.params import Depends, Path, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import HTTPException

from xpath_util import XpathUtil

from helpers import get_data_from_url_by_chromedriver, get_bs_data

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/get_xpath")
def get_xpath(url: str = Query(...)):
    content = get_data_from_url_by_chromedriver(url)
    soup = get_bs_data(content)
    xpath_obj = XpathUtil()
    xpath_data = xpath_obj.generate_xpath(soup)
    title = xpath_obj.get_title(soup)
    return {"title": title, "xpaths": xpath_data}
