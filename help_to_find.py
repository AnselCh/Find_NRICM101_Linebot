# -*- coding: utf-8 -*-
"""
為了更方便找尋提供公費(清冠一號)之中醫診所
藉由"國家中醫藥研究所"提供的"清冠一號動態表"
設計一套更方便的搜尋系統
@author: Ansel
"""
import requests
from bs4 import BeautifulSoup
import re

headers = {'user-agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
url="https://docs.google.com/spreadsheets/d/e/2PACX-1vQjf_HNeEZKM-XJX-q5v4cfNrB3kcv4gOT8kFbV9rurfoX_H5Qv9112Pv0PgYNFSzbReyNlQkLrJib3/pubhtml?utm_source=google&utm_medium=cpc&utm_campaign=%E6%B8%85%E5%86%A0%E4%B8%80%E8%99%9F%E5%8B%95%E6%85%8B%E8%A1%A8#"
html = requests.get(url,headers=headers)
if html.status_code == requests.codes.ok:
    get= BeautifulSoup(html.text, "lxml")
#抓出全台提供公費清冠一號的中醫診所 

data1=get.find('div',class_="ritz grid-container").tbody.find_all('tr')
#透過表格中輸入關鍵字列出想找的區域內的中醫
area = input(str("請輸入想查詢的區域或路名:"))
alldata = []
a=0


while True:
    
    if re.match("[\u4e00-\u9fa5]+",area) == None:
        print('請輸入正確的區域或路名')
        break
        
    
    for i in data1:
        alldata.append(i.find_all('td'))
    #print(len(alldata))    
    for j in alldata:
        
        if area in j[21].get_text() :
            search = j
            print('診所:%s\n電話:%s\n地址:%s' %(search[2].text,search[20].text,search[21].text))
            print('剩餘清冠一號數量(依廠牌顯示)')
            print('順天堂:%s'%search[3].text)
            print('莊松榮:%s'%search[4].text)
            print('立康:%s'%search[5].text)
            print('勝昌:%s'%search[6].text)
            print('勸奉堂:%s'%search[7].text)
            print('華佗:%s'%search[8].text)
            print('天一:%s'%search[9].text)
            print('漢聖:%s'%search[10].text)
            print('天明:%s'%search[11].text)
            print('科達:%s'%search[12].text)
            print('富田:%s'%search[13].text)
            print('-'*20)
            
        else:
            a +=1
    break
    if a == 1558:
        print('請輸入正確的區域或路名')
    




