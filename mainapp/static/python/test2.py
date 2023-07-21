import os
import sys
import urllib.request
import json

# Your client information
client_id = "l9u8XefecwXfibq5OoWU"
client_secret = "r6mCAuQK43"
url = "https://openapi.naver.com/v1/datalab/shopping/category/keyword/age"

# List of keywords, ages, and genders
keywords = ['유산균', '오메가3', '비오틴', '양배추즙', '글루타치온', '비타민d', '콘드로이친', '홍삼', '프로바이오틱스',
             '효소', '밀크씨슬', '멀티비타민', '마그네슘', '프로폴리스', '칼슘', '흑염소진액', '도라지배즙', '종합비타민',
             '코엔자임q10', '쏘팔메토', '세라티크', '엽산', '비트즙', '석류즙', '루테인', '꿀', 'msm', '비타민c', '호박즙',
             '프리바이오틱스', '링곤베리', '아연', '맥주효모', '양파즙', '보스웰리아', '칼슘마그네슘비타민d', '키크는영양제',
             '수국잎열수추출물', '배도라지즙', '사과즙', '이노시톨', '도라지청', '포스파티딜세린', '대마종자유', '장어즙', '새싹보리',
             '마카', '어린이비타민', '포스트바이오틱스', '수국잎추출물', '비타민b', '초록입홍합', '침향환', '블랙마카', '뇌영양제',
             '철분', '여주즙', '감마리놀렌산', '곡물효소', '활성엽산', '발효율피', '루테인지아잔틴', '꿀스틱', '관절영양제',
             '혈액순환영양제', '어린이영양제', '오쏘몰이뮨', '커큐민', '매스틱', '흑염소즙', '뉴질랜드초록홍합', '비타민',
             '숙취해소제', '로즈마리추출물', '비타민d추천', '정관장에브리타임', '벌집꿀', '위건강', '폴리코사놀', '기타건강즙/과일즙',
             '링곤베리퓨레', '여주환']
ages = ["10", "20", "30", "40", "50", "60"]
genders = ["f", "m"]

# Open a file to write the results
with open("results.txt", "w") as file:
    for keyword in keywords:
        for gender in genders:
            # Create the request body
            body = json.dumps({
                "startDate": "2018-01-01",
                "endDate": "2023-07-10",
                "timeUnit": "month",
                "category": "50000006",
                "keyword": keyword,
                "gender": gender,
                "ages": ages,
            })

            # Create the request
            request = urllib.request.Request(url)
            request.add_header("X-Naver-Client-Id", client_id)
            request.add_header("X-Naver-Client-Secret", client_secret)
            request.add_header("Content-Type","application/json")

            # Send the request
            response = urllib.request.urlopen(request, data=body.encode("utf-8"))
            rescode = response.getcode()

            if rescode == 200:
                response_body = response.read()
                result = response_body.decode('utf-8')
                file.write(f"Keyword: {keyword}, Gender: {gender}\n")
                file.write(result + "\n")
            else:
                file.write(f"Error Code: {rescode} for keyword: {keyword}, Gender: {gender}\n")
