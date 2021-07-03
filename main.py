from fastapi import FastAPI
from fastapi.params import Depends, Path, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import HTTPException

import helpers


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
    content = helpers.get_data_from_url_by_chromedriver(url)
    soup = helpers.get_bs_data(content)
    xpath_data = helpers.get_xpath(soup)
    title = helpers.get_title(soup)
    return {"title": title, "xpaths": xpath_data}
