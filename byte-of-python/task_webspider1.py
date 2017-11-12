# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup

response = requests.get("http://www.zkyouxi.com")
bs = BeautifulSoup(response.content, "html.parser")
for img in bs.findAll("img"):
    print img.get("src")

