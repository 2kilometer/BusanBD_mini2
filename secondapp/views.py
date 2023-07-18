from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

### secondapp의 최초 페이지 만들기
def getIndex(request):
    ### HTML 파일 사용..
    return render(request,
                  "secondapp/index.html",
                  {})

### index1 url 패턴 함수 생성
def getIndex2(request):
    msg = "<b>secondapp의 index2 페이지 입니다.</b>"
    return HttpResponse(msg)


### index02 url 패턴 함수 생성
def getIndex02(request):
    msg = "<b>getIndex02 :: 페이지 잘 호출 됩니다. </b>"
    return HttpResponse(msg)