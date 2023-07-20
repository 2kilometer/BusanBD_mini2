#-*- coding: utf-8 -*-
import os
import sys
import urllib.request
import pandas as pd
client_id = "l9u8XefecwXfibq5OoWU"
client_secret = "r6mCAuQK43"
url = "https://openapi.naver.com/v1/datalab/search";
body = (
    '{'
        '"startDate": "2017-01-01",'
        '"endDate": "2017-04-30",'
        '"timeUnit": "month",'
        '"keywordGroups": ['
            '{"groupName": "한글", "keywords": ["영양제", "nutritional supplements"]}'
        '],'
        '"device": "pc",'
        '"ages": ["1", "2"],'
        '"gender": "f"'
    '}'
)


request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
request.add_header("Content-Type","application/json")
response = urllib.request.urlopen(request, data=body.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)