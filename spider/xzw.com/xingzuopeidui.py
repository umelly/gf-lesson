# -*- coding: utf-8 -*-

"""男女星座配对
<option value="1">白羊座 (3.21-4.19)</option>
<option value="2">金牛座 (4.20-5.20)</option>
<option value="3">双子座 (5.21-6.21)</option>
<option value="4">巨蟹座 (6.22-7.22)</option>
<option value="5">狮子座 (7.23-8.22)</option>
<option value="6">处女座 (8.23-9.22)</option>
<option value="7">天秤座 (9.23-10.23)</option>
<option value="8">天蝎座 (10.24-11.22)</option>
<option value="9">射手座 (11.23-12.21)</option>
<option value="10">摩羯座 (12.22-1.19)</option>
<option value="11">水瓶座 (1.20-2.18)</option>
<option value="12">双鱼座 (2.19-3.20)</option>
"""

import requests
import psycopg2
from bs4 import BeautifulSoup

male_dict = {
    "1": "白羊座 (3.21-4.19)",
    "2": "金牛座 (4.20-5.20)",
    "3": "双子座 (5.21-6.21)",
    "4": "巨蟹座 (6.22-7.22)",
    "5": "狮子座 (7.23-8.22)",
    "6": "处女座 (8.23-9.22)",
    "7": "天秤座 (9.23-10.23)",
    "8": "天蝎座 (10.24-11.22)",
    "9": "射手座 (11.23-12.21)",
    "10": "摩羯座 (12.22-1.19)",
    "11": "水瓶座 (1.20-2.18)",
    "12": "双鱼座 (2.19-3.20)",
}

female_dict = male_dict

request_url = "http://www.xzw.com/cx/2/%s.html"

# sA + sB + sC + sD + lA + lB + lC + lD

lC = lD = ''
sC = sD = '0'
for male_k, male_v in male_dict.iteritems():
    lA = str(int(male_k)*2 + 2)
    sA = str(len(lA))
    for female_k, female_v in female_dict.iteritems():
        lB = str(int(female_k)*2 + 2)
        sB = str(len(lB))
        url = request_url % (sA + sB + sC + sD + lA + lB + lC + lD)
        dom = BeautifulSoup(requests.get(url).content, "html.parser")
        result_dom = dom.findAll("div", attrs={"class": "result"})[0]

        print "="*40, male_v, female_v, "="*40
        li_doms = result_dom.findAll("li")
        print li_doms[0].text
        print li_doms[1].text
        print li_doms[2].text
        print li_doms[3].text
        print li_doms[4].text
        print "\n"

        p_doms = result_dom.findAll("p")        
        print "恋爱建议:"
        print p_doms[0].text
        print "\n"

        print "注意事项:"
        print p_doms[1].text
        print "\n"

    #     break
    # break



"""
数据库
male_const 男生星座值
female_const 女生星座值

match_index 配对指数
match_weight 配对比重
...
"""


"""
import psycopg2

DB_URL = "postgresql://hef:@127.0.0.1:5432/dbname"

db = psycopg2.connect(DB_URL)
db_cursor = db.cursor()
db_cursor.execute("xxxx") // UPDATE INSERT DELETE SELECT
db_cursor.fetchall()/fetchone() // SELECT
"""
