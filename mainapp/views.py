from django.shortcuts import render
from .DB_Sql import disease, user
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Users, Userdis, Prod, Disease

# Create your views here.

# mainapp에서 최초 호출 함수로 사용..

def index(request):
    return render(request,
                  "mainapp/index.html",
                  {})

def logout_chk (request) :
    request.session.flush()
    
    msg = """
        <script type='text/javascript'>
            alert('로그아웃 되었습니다.');
            location.href = '/';
        </script>
    """
    return HttpResponse (msg)

def login_chk (request) :
    user_id = request.POST.get("user_id","")
    user_pw = request.POST.get("user_pw","")
    
    user_view = user.getLoginChk(user_id, user_pw)

    if user_view.get("result") == "None" :
        msg = """
            <script type='text/javascript'>
                alert('회원정보가 일치하지 않습니다. 다시 입력해 주세요!');
                location.href = '/recom/';
            </script>
        """
        return HttpResponse(msg)
    
    msg = " {} / {} ".format(user_view["user_id"],
                                  user_view["user_pw"])
    
    request.session["ses_user_id"] = user_id

    msg = """
        <script type='text/javascript'>
            alert('환영합니다. 로그인 되었습니다.');
            location.href = '/';
        </script>
    """
    
    return HttpResponse (msg)

def Register(request):
    
    dis_list = disease.dis_list()
    dis_middle = disease.dis_middle()
    
    return render(request,
                  "mainapp/register.html",
                  {"dis_list" : dis_list,
                   "dis_middle" : dis_middle,
                   })

# def Register1(request) :    
#     age = request.POST.get("age", "")
#     if age != "":
#         dis_age = disease.dis_age(age)
#     else:
#         dis_age = disease.dis_age('10대')
#     return render(request,
#                   "mainapp/register1.html",
#                   {"dis_age" : dis_age,})
def Register1(request):
    # POST 데이터로부터 나이(age) 가져오기
    age = request.POST.get("age", "")

    # 디버깅을 위해 전체 POST 데이터 출력
    print("POST 데이터:", request.POST)

    # 디버깅을 위해 나이(age) 값 출력
    print("나이:", age)

    if age != "":
        dis_age = disease.dis_age(age)
    else:
        dis_age = disease.dis_age('10대')

    return render(request, "mainapp/register1.html", {"dis_age": dis_age})


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
