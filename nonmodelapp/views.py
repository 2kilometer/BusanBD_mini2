from django.shortcuts import render
from django.http import HttpResponse
from .DB_Sql import disease
from .DB_Sql import sign_in
from .DB_Sql import user
from .DB_Sql import recom
from django.core.paginator import Paginator
from .models import Users, Userdis, Prod, Disease


def index(request):
    return render(request,
                  "nonmodelapp/index.html",
                  {})

def about(request):
    return render(request,
                  "nonmodelapp/about.html",
                  {})
    
def contact(request):
    
    dis_list = disease.dis_list()
    dis_middle = disease.dis_middle()
    return render(request,
                  "nonmodelapp/contact.html",
                  {"dis_list" : dis_list,
                   "dis_middle" : dis_middle,})

def doctor(request):
    return render(request,
                  "nonmodelapp/doctor.html",
                  {})
    
def testimonial(request):
    return render(request,
                  "nonmodelapp/testimonial.html",
                  {})

def treatment(request):
    return render(request,
                  "nonmodelapp/treatment.html",
                  {})
    
def Register1(request):
    # POST 데이터로부터 나이(age) 가져오기
    age = request.GET.get("age", "")
    gender = request.GET.get("gender", "")

    if age != "" and gender != "":
        dis_age = disease.dis_age(age, gender)
    
    else :
        dis_age = age
    

    return render(request, "nonmodelapp/register1.html", {"dis_age": dis_age})

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