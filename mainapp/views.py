from django.shortcuts import render
from .DB_Sql import disease

# Create your views here.

# mainapp에서 최초 호출 함수로 사용..
def setCartInsert (request) :
    try :
        cart_member = request.POST.get("cart_member")
        cart_no = request.POST.get("cart_no")
        cart_prod = request.POST.get("cart_prod")
        cart_qty = request.POST.get("cart_qty")
        
        Cart.objects.filter(cart_no = cart_no,
                            cart_prod = cart_prod).create(cart_member = cart_member,
                                                          cart_no = cart_no,
                                                          cart_prod = cart_prod,
                                                          cart_qty = cart_qty)

        msg = """
            <script type = 'text/javascript'>
                alert('정상적으로 입력되었습니다');
                location.href = '/oracle/cart_list/';
            </script>
        """
        return HttpResponse (msg)
    
    except :
        msg = """
            <script type = 'text/javascript'>
                alert('오류발생');
                history.go(-1);
            </script>
        """
        return HttpResponse (msg)

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
