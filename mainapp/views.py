from django.shortcuts import render
from django.http import HttpResponse
from .DB_Sql import disease
from .DB_Sql import sign_in
from .DB_Sql import user
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
    

def Register1(request):
    # POST 데이터로부터 나이(age) 가져오기
    age = request.GET.get("age", "")
    gender = request.GET.get("gender", "")

    # 디버깅을 위해 전체 POST 데이터 출력
    print("POST 데이터:", request.POST)

    # 디버깅을 위해 나이(age) 값 출력
    print("나이:", age)

    if age != "" and gender != "":
        dis_age = disease.dis_age(age, gender)
    
    else :
        dis_age = age
    

    return render(request, "mainapp/register1.html", {"dis_age": dis_age})



def sign(request):
    try :
        email   = request.POST.get("email")
        password   = request.POST.get("password")
        age = request.POST.get("age")
        gender   = request.POST.get("gender")
        stress   = request.POST.get("stress")
        dis_id   = request.POST.getlist("dis_id")
        dis_id2   = request.POST.getlist("dis_id2")
        dis_middle   = request.POST.getlist("dis_middle")
        sign_in.sign_up(email, password, age, gender, stress)

        # 두 리스트를 합칩니다
        total_dis_id = dis_id + dis_id2

        # 중복 항목을 제거하기 위해 set으로 변환하고, 다시 list로 변환합니다
        sum_dis = list(set(total_dis_id))
        dis_middle = list(set(dis_middle))
        
        for i in range(len(sum_dis)):
            sign_in.ud_dis(email ,sum_dis[i])
            
        for d in range(len(dis_middle)):
            sign_in.middle(email ,dis_middle[d])
        
    except :        
        ### 오류처리
        msg = """
            <script type='text/javascript'>
                alert('오류발생{},{},{},{},{}');
                history.go(-1);
            </script>
        """.format(id, password, age, gender, stress)   
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
    user_list = Users.objects.all()
    return render(request,
                  "mainapp/recom.html",
                  {"user_list" : user_list})

def Statistic(request):
    return render(request,
                  "mainapp/statistic.html",
                  {})
