# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 22:07:16 2022
合併
@author: annann
"""

import json  

with open('findmed.json',encoding="utf-8") as f1, open('geocode.json',encoding="utf-8") as f2:
    first_list = json.load(f1)
    second_list = json.load(f2)

for i, v in enumerate(first_list):
    second_list[i].update(v)
    
with open("final.json", "w",encoding = 'utf-8') as file:
    json.dump(second_list, file, indent = 4, ensure_ascii=False)

