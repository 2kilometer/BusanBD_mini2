from django.shortcuts import render
from django.http import HttpResponse
from .DB_Sql import disease
from .DB_Sql import sign_in
from .DB_Sql import user
from .DB_Sql import recom
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
        email   = request.POST.get("email","")
        password   = request.POST.get("password","")
        age = request.POST.get("age","")
        gender   = request.POST.get("gender","")
        stress   = request.POST.get("stress","")
        dis_id   = request.POST.getlist("dis_id","")
        dis_id2   = request.POST.getlist("dis_id2","")
        dis_middle   = request.POST.getlist("dis_middle","")
        
        if email != "":
            sign_in.sign_up(email, password, age, gender, stress)
            
            total_dis_id = dis_id + dis_id2
            
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
                alert('오류발생{}{}');
            </script>
        """
        return HttpResponse(msg)
    
    ### 정상처리
    msg = """
        <script type='text/javascript'>
            alert('정상적으로 입력되었습니다!!');
            history.go(-1);
        </script>
    """   
    return HttpResponse(msg)


def dis_add(request):
    try:
        user_dis   = request.POST.getlist("user_dis","")
        user_id   = request.POST.get("user_id","")
        dis_middle   = request.POST.get("dis_middle","")
        if user_dis != "":
            for i in range(len(user_dis)):
                sign_in.ud_dis(user_id ,user_dis[i])
        if dis_middle != "":
            for i in range(len(dis_middle)):
                sign_in.ud_dis(user_id , dis_middle[i])
    except :        
        ### 오류처리
        msg = """
            <script type='text/javascript'>
                alert('오류발생{}/{}');
            </script>
        """.format(user_dis, user_id)  
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

def Recom_dis(request):
    id = request.GET.get("id", "")
    recom_pill = recom.user_info(id)
    recom_pill2 = recom.user_info2(id)
    
    merged_list = recom_pill
    for pill in recom_pill2:
        if pill not in merged_list:
            merged_list.append(pill)
    
    return render(request,
                  "mainapp/recom_dis.html",
                  {"merged_list": merged_list})


def prodprod(request):
    prod_name = request.GET.get("prod_name", "")
    prod_info = recom.prod_info(prod_name)
    
    return render(request,
                  "mainapp/prodprod.html",
                  {"prod_info": prod_info})

def naver(request):
    id = request.GET.get("id", "")
    
    naver_info = recom.naver(id)
    
    return render(request,
                  "mainapp/naver.html",
                  {"naver_info": naver_info})

##질병 추가하기 함수
def Insert_view(request):
    id = request.GET.get("id", "")
    dis_all = disease.dis_list()
    
    if id != "" :
        dis_id = recom.insert_dis(id)
    
    else :
        dis_id = dis_id
     # dis_id 리스트에서 'ud_dis' 키의 값을 추출하여 새 리스트 생성
    dis_id_values = [dis['ud_dis'] for dis in dis_id]

    # Create a new list containing only elements of dis_all that are not in dis_id_values
    dis_new = [dis for dis in dis_all if dis['dis_id'] not in dis_id_values]

    return render(request, "mainapp/insert_dis.html", {"dis_list": dis_id,
                                                       "dis_new" : dis_new})
    
def Insert_view2(request):
    id = request.GET.get("id", "")
    dis_all = disease.dis_middle()
    
    if id != "" :
        dis_id = recom.insert_middle(id)
    
    else :
        dis_id = dis_id
     # dis_id 리스트에서 'ud_dis' 키의 값을 추출하여 새 리스트 생성
     
    dis_id_values = [dis['md_middle'] for dis in dis_id]
     
    dis_new = [dis for dis in dis_all if dis['dis_middle'] not in dis_id_values]

    return render(request, "mainapp/insert_dis2.html", {"dis_list": dis_id,
                                                       "dis_new" : dis_new})

def Statistic(request):
    return render(request,
                  "mainapp/statistic.html",
                  {})
