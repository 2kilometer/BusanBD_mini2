from django.shortcuts import render

# Create your views here.
### 웹프로그램 최초에 작성하는 파일 ****
# - views.py 내에 작성하는 모든 프로그램은
#   함수로 만들어야 합니다.
# - 장고 웹프로그램은 함수 호출기반으로 구조화됨
# - 기본 라이브러리 : HttpResponse
from django.http import HttpResponse

### HTML파일에 데이터를 넘겨서 출력 시키기
def getTemplate01(request):
    mem_name = "이순신"
    mem_add  = "부산 수영구~~"
    return render(request,
                  "firstapp/template01.html",
                  ### front 프로그램 영역으로 데이터를 전달하는 곳
                  # - key는 문자열로 보통 정의
                  # - value는 변수 또는 직접 값을 넣어줘도 됨
                  {"mem_name" : mem_name,
                   "mem_add" : mem_add})

### 함수 생성 : 함수 1개당 웹페이지 1개라고 인지..
def index(request):
    ### request : 클라이언트 요청을 받아오기
    #   - 요청 정보가 request에 들어있음
    #   - 요청에 대한 응답은 response 
    # return HttpResponse("<b>안녕하세요~ 장고...</b>")
    
    ### HTML 파일을 만들어서 사용하는 경우에는 render()함수 사용
    return render(request,
                  ### html 파일 위치 지정
                  "firstapp/index.html",
                  ### 데이터를 html에서 출력하고자 할 때 지정
                  # - key : value의 딕셔너리 타입으로 사용됨
                  # - key는 변수로 사용됨, 
                  # - value는 값으로 사용됨
                  {})
    

### 함수 생성
def getIndex1(request):
    ### 응답 내용 처리하기
    msg = "<b>firstapp/urls.py : index1 페이지 입니다.</b>"
    return HttpResponse(msg)