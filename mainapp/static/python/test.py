import os
import sys
import urllib.request

client_id = "l9u8XefecwXfibq5OoWU"
client_secret = "r6mCAuQK43"
url = "https://openapi.naver.com/v1/datalab/shopping/category/keyword/age"

keywords = ['마그네슘', '유산균', '오메가3', '비오틴']
genders = ['m', 'f']

for gender in genders:
    for keyword in keywords:
        body = (
            '{'
                '"startDate": "2023-01-01",'
                '"endDate": "2023-07-10",'
                '"timeUnit": "month",'
                '"category": "50000006",'
                "keyword": [{"name": "식품/건강식품", "param": [keyword]}],
                '"ages": ["10","20","30","40","50","60"],'
                '"gender": "' + gender + '"'
            '}'
        )

        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id", client_id)
        request.add_header("X-Naver-Client-Secret", client_secret)
        request.add_header("Content-Type","application/json")
        response = urllib.request.urlopen(request, data=body.encode("utf-8"))
        rescode = response.getcode()
        if rescode == 200:
            response_body = response.read()
            print(response_body.decode('utf-8'))
        else:
            print("Error Code:" + str(rescode))
