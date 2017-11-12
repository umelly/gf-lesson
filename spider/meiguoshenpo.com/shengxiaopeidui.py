# -*- coding: utf-8 -*-

"""生肖配对
<option value="1">男生-属鼠</option>
<option value="2">男生-属牛</option>
<option value="3">男生-属虎</option>
<option value="4">男生-属兔</option>
<option value="5">男生-属龙</option>
<option value="6">男生-属蛇</option>
<option value="7">男生-属马</option>
<option value="8">男生-属羊</option>
<option value="9">男生-属猴</option>
<option value="10">男生-属鸡</option>
<option value="11">男生-属狗</option>
<option value="12">男生-属猪</option>

### 流程说明
男生肖 SX_PEIDUI_1
女生肖 SX_PEIDUI_2

1. 获取男女生肖值SX_PEIDUI_1，SX_PEIDUI_2
2. 向http://www.meiguoshenpo.com/tool/shengxiao_peidui.html发起GET请求
3. 服务器跳到http://www.meiguoshenpo.com/shengxiao/peidui/shu_shu.html
"""

import requests
from bs4 import BeautifulSoup

male_sx_dict = {
    "1": "属鼠",
    "2": "属牛",
    "3": "属虎",
    "4": "属兔",
    "5": "属龙",
    "6": "属蛇",
    "7": "属马",
    "8": "属羊",
    "9": "属猴",
    "10": "属鸡",
    "11": "属狗",
    "12": "属猪",
}

female_sx_dict = male_sx_dict
headers = {
    "Referer": "http://www.meiguoshenpo.com/shengxiao/peidui/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
}

request_url = "http://www.meiguoshenpo.com/tool/shengxiao_peidui.html"
for male_k, male_v in male_sx_dict.iteritems():
    for female_k, female_v in female_sx_dict.iteritems():
        print "="*40, "(男)"+male_v, "(女)"+female_v, "="*40
        params = {
           "SX_PEIDUI_1": male_k,
           "SX_PEIDUI_2": female_k, 
        }
        response = requests.head(request_url, params=params)
        result_url = response.next.url

        response = requests.get(result_url)
        dom = BeautifulSoup(response.content, "html.parser")
        result_dom = dom.findAll("div", attrs={"class": "show_cnt"})[0]
        for p_dom in result_dom.findAll("p"):
            print p_dom.text

        break
    break
