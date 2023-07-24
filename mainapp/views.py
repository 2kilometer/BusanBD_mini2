from django.shortcuts import render
from django.http import HttpResponse
from .DB_Sql import disease
from .DB_Sql import sign_in

# Create your views here.

# mainapp에서 최초 호출 함수로 사용..


def index(request):
    return render(request,
                  "mainapp/index.html",
                  {})


def Register(request):
    
    dis_list = disease.dis_list()
    dis_middle = disease.dis_middle()
    
    return render(request,
                  "mainapp/register.html",
                  {"dis_list" : dis_list,
                   "dis_middle" : dis_middle,
                   })
    

def Register1(request):
    # POST 데이터로부터 나이(age) 가져오기
    age = request.GET.get("age", "")

    # 디버깅을 위해 전체 POST 데이터 출력
    print("POST 데이터:", request.POST)

    # 디버깅을 위해 나이(age) 값 출력
    print("나이:", age)

    if age != "":
        dis_age = disease.dis_age(age)
    
    else :
        dis_age = age

    return render(request, "mainapp/register1.html", {"dis_age": dis_age})



def sign_in(request):
    try :
        email   = request.POST.get("email")
        password   = request.POST.get("password")
        age = request.POST.get("age")
        gender   = request.POST.get("gender")
        stress   = request.POST.get("stress")
        sign_in.sign_up(email, password, age, gender, stress)
        
    except :        
        ### 오류처리
        msg = """
            <script type='text/javascript'>
                alert('오류발생{},{},{},{},{}');
                history.go(-1);
            </script>
        """.format(email, password, age, gender, stress)   
        return HttpResponse(msg)
    
    ### 정상처리
    msg = """
        <script type='text/javascript'>
            alert('정상적으로 입력되었습니다!!');
            location.href='/recom/';
        </script>
    """   
    return HttpResponse(msg)



def Data_info(request):
    return render(request,
                  "mainapp/data_info.html",
                  {})

def Recom(request):
    return render(request,
                  "mainapp/recom.html",
                  {})

def Statistic(request):
    return render(request,
                  "mainapp/statistic.html",
                  {})
