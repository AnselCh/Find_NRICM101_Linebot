# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 13:53:22 2022

@author: annann
all ver
"""

import requests, re, json
from bs4 import BeautifulSoup

class Find(object):

    def __init__(self):
        self.baseurl =  'https://docs.google.com'
        self.starturl = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQjf_HNeEZKM-XJX-q5v4cfNrB3kcv4gOT8kFbV9rurfoX_H5Qv9112Pv0PgYNFSzbReyNlQkLrJib3/pubhtml?utm_source=google&utm_medium=cpc&utm_campaign=%E6%B8%85%E5%86%A0%E4%B8%80%E8%99%9F%E5%8B%95%E6%85%8B%E8%A1%A8#' # 初始url
    
    def start_requests(self, url): 
        r = requests.get(url)
        return r.content

    def parse(self, text): 
        soup = BeautifulSoup(text, 'html.parser')
        divs = soup.find('div',class_="ritz grid-container").tbody.find_all('tr')
        
        alldata = []
        while True:
            for i in divs:
                alldata.append(i.find_all('td'))
            #print(len(alldata))    
            for j in alldata:
                    search = j
                    yield{
                       'name':search[2].text,
                       'phone':search[20].text,
                       'address':search[21].text,
                       'updated':search[14].text,
                       'brand1':search[3].text,
                       'brand2':search[4].text,
                       'brand3':search[5].text,
                       'brand4':search[6].text,
                       'brand5':search[7].text,
                       'brand6':search[8].text,
                       'brand7':search[9].text,
                       'brand8':search[10].text,
                       'brand9':search[11].text,
                       'brand10':search[12].text,
                       'brand11':search[13].text,
                       
                      }
            break       

                
    def start(self):
        text = self.start_requests(self.starturl)
        items = self.parse(text)
        
        s = json.dumps(list(items), indent = 4, ensure_ascii=False)
        with open('findmed.json', 'w', encoding = 'utf-8') as f:
            f.write(s)

find = Find()
find.start()

                    
#原来路径：https://github.com/Fendouzhe/lwwJson/blob/master/lww.json
#改后路径：https://raw.githubusercontent.com/Fendouzhe/lwwJson/master/lww.json

  
# https://raw.githubusercontent.com/AnselCh/Find_NRICM101/main/FindMedwithGeo.json                
                    
                    
                    