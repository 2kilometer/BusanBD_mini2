from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

### models.py에 생성한 Member 클래스 불러들이기
from .models import Member, Cart, Lprod, Prod, CartMember, CartMemberProd

############ [상품검색에 따른 주문정보 조회 및 저장하기] ############
############ [주문 + 회원정보 + 상품정보 관리] ############
### 주문 + 회원정보 + 상품정보 전체 조회하기
def getProductList(request):
    cart_list = CartMemberProd.objects.all().order_by("-cart_no", "cart_member")
    return render(request, 
                  "oracleapp/product/cart_mem_prod_list.html",
                  {"cart_list" : cart_list})
    
    
### 상품검색에 따른 주문정보 저장하기
def setProductInsert(request):   
    try :
        cart_no     = "2023071400002"
        cart_member   = "a001"
        cart_prod   = request.POST.get("prod_id")
        cart_qty   = request.POST.get("cart_qty")
        
        Cart.objects.create(cart_no = cart_no,                            
                            cart_member = cart_member,
                            cart_prod = cart_prod,
                            cart_qty = cart_qty)
    except :        
        ### 오류처리
        msg = """
            <script type='text/javascript'>
                alert('오류발생');
                history.go(-1);
            </script>
        """    
        return HttpResponse(msg)
    
    ### 정상처리
    msg = """
        <script type='text/javascript'>
            alert('정상적으로 입력되었습니다!!');
            location.href='/oracle/cart_list/';
        </script>
    """   
    return HttpResponse(msg)

### [상품검색에 따른 주문정보 조회 하기] ############
### - 조별실습.ppt 화면 참고..
def getProduct(request):
    lprod_gu = request.POST.get("lprod_gu", "")
    prod_id  = request.POST.get("prod_id", "")
    change  = request.POST.get("change", "False")
    
    ### 상품분류 select option태그 내용 조회
    lprod_selbox = Lprod.objects.all().order_by("lprod_id") 

    if lprod_gu == "" : 
        ### 상품 select option태그 내용 조회 : 최초 페이지 로딩시
        prod_selbox  = Prod.objects.filter(prod_lgu = lprod_selbox[0].lprod_gu)
        lprod_gu = lprod_selbox[0].lprod_gu
        prod_id  = prod_selbox[0].prod_id
        
    else :
        ### 상품 select option태그 내용 조회 : 상품분류가 선택되었을 때
        prod_selbox  = Prod.objects.filter(prod_lgu = lprod_gu)
    
    ### 검색 버튼이 클릭 되었을 때만 조회시키기
    if change == "True" :
        prod_view = Prod.objects.get(prod_id = prod_id)
        
    ### 검색 버튼이 클릭 되지 않으면, 조회 안시키기
    # - 아래 딕셔너리에 변수는 무조건 넣어주어야 하기 때문에 
    #   형태만 갖추어서 넣어주었을 뿐임..
    else :
        prod_view = {"" : ""}
            
    return render(request, 
                  "oracleapp/product/product.html",
                  {"lprod_selbox" : lprod_selbox,
                   "prod_selbox" : prod_selbox,
                   "lprod_gu" : lprod_gu,
                   "prod_id" : prod_id,
                   "prod_view" : prod_view,
                   "change" : change})
    
    

############ [주문 + 회원정보 + 상품정보 관리] ############
### 주문 + 회원정보 + 상품정보 전체 조회하기
def getCartMemProdList(request):
    ### order_by : 정렬
    # - 문자열로 작성
    # - 오름차순을 컬럼명 그대로
    # - 내림차순은 컬럼명 왼쪽에 마이너스(-) 표시
    cart_list = CartMemberProd.objects.all().order_by("-cart_no", "cart_member")
    return render(request, 
                  "oracleapp/cartmem/cart_mem_prod_list.html",
                  {"cart_list" : cart_list})
    

############ [주문 + 회원정보 관리] ############
### 주문 + 회원정보 전체 조회하기
def getCartMemList(request):
    ### order_by : 정렬
    # - 문자열로 작성
    # - 오름차순을 컬럼명 그대로
    # - 내림차순은 컬럼명 왼쪽에 마이너스(-) 표시
    cart_list = CartMember.objects.all().order_by("-cart_no", "cart_member")
    return render(request, 
                  "oracleapp/cartmem/cart_mem_list.html",
                  {"cart_list" : cart_list})


############ [상품정보 관리] ############

### 상품정보 수정하기
def setProdUpdate(request):    
    try :
        prod_id    = request.POST.get("prod_id")
        prod_name  = request.POST.get("prod_name")
        prod_cost  = request.POST.get("prod_cost")
        prod_price = request.POST.get("prod_price")
        prod_sale  = request.POST.get("prod_sale")
        
        Prod.objects.filter(prod_id = prod_id).update(prod_name = prod_name,
                                                       prod_cost = prod_cost,
                                                       prod_price = prod_price,
                                                       prod_sale = prod_sale)
        
    except :        
        ### 오류처리
        msg = """
            <script type='text/javascript'>
                alert('오류발생');
                history.go(-1);
            </script>
        """    
        return HttpResponse(msg)
    
    ### 정상처리
    msg = """
        <script type='text/javascript'>
            alert('정상적으로 수정되었습니다!!');
            location.href='/oracle/prod_view/?prod_id={}';
        </script>
        """.format(prod_id)   
     
    return HttpResponse(msg)


### 상품정보 수정페이지 조회하기
def getProdUpdateView(request):    
    prod_id   = request.GET.get("prod_id")
    
    prod_view = Prod.objects.get(prod_id = prod_id)
    
    return render(request, 
                  "oracleapp/prod/prod_update_view.html",
                  {"prod_view" : prod_view,
                   "prod_id" : prod_id})


### 상품정보 상세조회하기
def getProdView(request):    
    prod_id   = request.GET.get("prod_id")
    
    prod_view = Prod.objects.get(prod_id = prod_id)
    
    return render(request, 
                  "oracleapp/prod/prod_view.html",
                  {"prod_view" : prod_view,
                   "prod_id" : prod_id})
    
### 상품정보 전체조회하기
def getProdList(request):
    ### order_by : 정렬
    # - 문자열로 작성
    # - 오름차순을 컬럼명 그대로
    # - 내림차순은 컬럼명 왼쪽에 마이너스(-) 표시
    prod_list = Prod.objects.all().order_by("prod_id")
    return render(request, 
                  "oracleapp/prod/prod_list.html",
                  {"prod_list" : prod_list})


############ [상품분류정보 관리] ############

### 상품분류정보 입력 처리하기
def setLprodInsert(request):    
    try :
        lprod_gu   = request.POST.get("lprod_gu")
        lprod_id   = request.POST.get("lprod_id")
        lprod_nm   = request.POST.get("lprod_nm")
        
        Lprod.objects.create(lprod_gu = lprod_gu,                            
                            lprod_id = lprod_id,
                            lprod_nm = lprod_nm)
    except :        
        ### 오류처리
        msg = """
            <script type='text/javascript'>
                alert('오류발생');
                history.go(-1);
            </script>
        """    
        return HttpResponse(msg)
    
    ### 정상처리
    msg = """
        <script type='text/javascript'>
            alert('정상적으로 입력되었습니다!!');
            location.href='/oracle/lprod_list/';
        </script>
    """    
    # msg = "{} / {} / {}".format(lprod_gu, lprod_id, lprod_nm)
    return HttpResponse(msg)


### 상품분류정보 입력을 위한 view 페이지
def getLprodInsertView(request):  
    return render(request, 
                  "oracleapp/lprod/lprod_insert_view.html",
                  {})    

### 상품분류정보 수정하기
def setLprodUpdate(request):    
    try :
        lprod_gu   = request.POST.get("lprod_gu")
        lprod_id   = request.POST.get("lprod_id")
        lprod_nm   = request.POST.get("lprod_nm")
        
        Lprod.objects.filter(lprod_gu = lprod_gu).update(lprod_id = lprod_id,
                                                         lprod_nm = lprod_nm)
        
    except :        
        ### 오류처리
        msg = """
            <script type='text/javascript'>
                alert('오류발생');
                history.go(-1);
            </script>
        """    
        return HttpResponse(msg)
    
    ### 정상처리
    msg = """
        <script type='text/javascript'>
            alert('정상적으로 수정되었습니다!!');
            location.href='/oracle/lprod_view/?lprod_gu={}';
        </script>
    """.format(lprod_gu)   
     
    return HttpResponse(msg)


### 상품분류정보 수정페이지 조회하기
def getLprodUpdateView(request):    
    lprod_gu   = request.GET.get("lprod_gu")
    
    lprod_view = Lprod.objects.get(lprod_gu = lprod_gu)
    
    return render(request, 
                  "oracleapp/lprod/lprod_update_view.html",
                  {"lprod_view" : lprod_view,
                   "lprod_gu" : lprod_gu})

### 상품분류정보 삭제하기
def setLprodDelete(request):    
    try :
        lprod_gu   = request.GET.get("lprod_gu")
        
        Lprod.objects.filter(lprod_gu = lprod_gu).delete()
        
    except :        
        ### 오류처리
        msg = """
            <script type='text/javascript'>
                alert('오류발생');
                history.go(-1);
            </script>
        """    
        return HttpResponse(msg)
    
    ### 정상처리
    msg = """
        <script type='text/javascript'>
            alert('정상적으로 삭제되었습니다!!');
            location.href='/oracle/lprod_list/';
        </script>
    """    
    return HttpResponse(msg)



### 상품분류정보 상세조회하기
def getLprodView(request):    
    lprod_gu   = request.GET.get("lprod_gu")
    
    lprod_view = Lprod.objects.get(lprod_gu = lprod_gu)
    
    return render(request, 
                  "oracleapp/lprod/lprod_view.html",
                  {"lprod_view" : lprod_view,
                   "lprod_gu" : lprod_gu})
    
### 상품분류정보 전체조회하기
def getLprodList(request):
    ### order_by : 정렬
    # - 문자열로 작성
    # - 오름차순을 컬럼명 그대로
    # - 내림차순은 컬럼명 왼쪽에 마이너스(-) 표시
    lprod_list = Lprod.objects.all().order_by("lprod_gu")
    return render(request, 
                  "oracleapp/lprod/lprod_list.html",
                  {"lprod_list" : lprod_list})



############ [주문정보 관리] ############

### 주문정보 입력 처리하기
def setCartInsert(request):    
    try :
        cart_no     = request.POST.get("cart_no")
        cart_member   = request.POST.get("cart_member")
        cart_prod   = request.POST.get("cart_prod")
        cart_qty   = request.POST.get("cart_qty")
        
        ### SQL
        # Insert Into cart(cart_no, cart_member, cart_prod, cart_qty) 
        #  values(cart_no값, cart_member값, cart_prod값, cart_qty값)
        Cart.objects.create(cart_no = cart_no,                            
                            cart_member = cart_member,
                            cart_prod = cart_prod,
                            cart_qty = cart_qty)
    except :        
        ### 오류처리
        msg = """
            <script type='text/javascript'>
                alert('오류발생');
                history.go(-1);
            </script>
        """    
        return HttpResponse(msg)
    
    ### 정상처리
    msg = """
        <script type='text/javascript'>
            alert('정상적으로 입력되었습니다!!');
            location.href='/oracle/cart_list/';
        </script>
    """   
    return HttpResponse(msg)


### 주문정보 입력을 위한 view 페이지
def getCartInsertView(request):  
    return render(request, 
                  "oracleapp/cart/cart_insert_view.html",
                  {})    

### 주문정보 수정하기
def setCartUpdate(request):    
    try :
        cart_no     = request.POST.get("cart_no")
        cart_prod   = request.POST.get("cart_prod")
        cart_qty   = request.POST.get("cart_qty")
        
        ### SQL
        # Update cart
        #   Set cart_qty = cart_qty변수값
        # Where cart_no = cart_no값
        #   And cart_prod = cart_prod값
        Cart.objects.filter(cart_no = cart_no,
                            cart_prod = cart_prod).update(cart_qty = cart_qty)
    except :        
        ### 오류처리
        msg = """
            <script type='text/javascript'>
                alert('오류발생');
                history.go(-1);
            </script>
        """    
        return HttpResponse(msg)
    
    ### 정상처리
    msg = """
        <script type='text/javascript'>
            alert('정상적으로 수정되었습니다!!');
            location.href='/oracle/cart_view/?cart_no={}&cart_prod={}';
        </script>
    """.format(cart_no, cart_prod)    
    return HttpResponse(msg)

### 주문정보 수정페이지 조회하기
def getCartUpdateView(request):    
    cart_no     = request.GET.get("cart_no")
    cart_prod   = request.GET.get("cart_prod")
    
    ### SQL
    # Select cart_no, cart_member, cart_prod, cart_qty
    # From cart
    # Where cart_no = cart_no변수
    #   And cart_prod = cart_prod변수
    cart_view = Cart.objects.get(cart_no = cart_no,
                                 cart_prod = cart_prod)
    
    return render(request, 
                  "oracleapp/cart/cart_update_view.html",
                  {"cart_view" : cart_view,
                   "cart_no" : cart_no,
                   "cart_prod" : cart_prod})

### 주문정보 삭제하기
def setCartDelete(request):    
    try :
        cart_no     = request.GET.get("cart_no")
        cart_prod   = request.GET.get("cart_prod")
        
        ### SQL
        # Delete From cart
        # Where cart_no = cart_no값
        #   And cart_prod = cart_prod값
        Cart.objects.filter(cart_no = cart_no,
                            cart_prod = cart_prod).delete()
    except :        
        ### 오류처리
        msg = """
            <script type='text/javascript'>
                alert('오류발생');
                history.go(-1);
            </script>
        """    
        return HttpResponse(msg)
    
    ### 정상처리
    msg = """
        <script type='text/javascript'>
            alert('정상적으로 삭제되었습니다!!');
            location.href='/oracle/cart_list/';
        </script>
    """    
    return HttpResponse(msg)



### 주문정보 상세조회하기
def getCartView(request):    
    cart_no     = request.GET.get("cart_no")
    cart_prod   = request.GET.get("cart_prod")
    
    ### SQL
    # Select cart_no, cart_member, cart_prod, cart_qty
    # From cart
    # Where cart_no = cart_no변수
    #   And cart_prod = cart_prod변수
    cart_view = Cart.objects.get(cart_no = cart_no,
                                 cart_prod = cart_prod)
    
    return render(request, 
                  "oracleapp/cart/cart_view.html",
                  {"cart_view" : cart_view,
                   "cart_no" : cart_no,
                   "cart_prod" : cart_prod})
    
### 주문정보 전체조회하기
def getCartList(request):
    ### order_by : 정렬
    # - 문자열로 작성
    # - 오름차순을 컬럼명 그대로
    # - 내림차순은 컬럼명 왼쪽에 마이너스(-) 표시
    cart_list = Cart.objects.all().order_by("-cart_no", "cart_member")
    return render(request, 
                  "oracleapp/cart/cart_list.html",
                  {"cart_list" : cart_list})


############ [회원관리] ############
### 회원정보 수정하기
# - 수정에 대한 처리는 Database 처리후 상세보기 페이지로 이동만 하면됨
# - 별도의 html 페이지가 필요 없습니다.(render 사용하지 않아도 됨)
def setMemberUpdate(request):
    try :
        mem_id = request.POST.get("mem_id")
        mem_pass = request.POST.get("mem_pass")
        mem_add1 = request.POST.get("mem_add1")
        
        ### Member 클래스에서 행(objects) 전체(all) 조회하기
        
        # Update member
        #    Set mem_pass = mem_pass변수,
        #        mem_add1 = mem_add1변수
        # Where mem_id = mem_id변수
        ###(해석) member테이블의 데이터 중에 아이디가 mem_id변수인 것에 대한
        #         mem_pass 컬럼의 값을 mem_pass변수의 값으로 수정
        #         그리고, mem_add1 컬럼의 값을 mem_add1변수의 값으로 수정
        
        Member.objects.filter(mem_id = mem_id).update(mem_pass=mem_pass,
                                                    mem_add1=mem_add1)
    except :
        ### 오류처리
        msg = """
            <script type='text/javascript'>
                alert('오류발생');
                history.go(-1);
            </script>
        """    
        return HttpResponse(msg)
    
    ### 정상처리
    # msg = "{} / {} / {}".format(mem_id, mem_pass, mem_add1)
    msg = """
        <script type='text/javascript'>
            alert('정상적으로 수정되었습니다!!');
            location.href='/oracle/mem_view/?mem_id={}';
        </script>
    """.format(mem_id)
    
    return HttpResponse(msg)

    
### 회원정보 수정페이지 조회하기
def getMemberUpdateView(request):
    mem_id = request.GET.get("mem_id")
    
    ### Member 클래스에서 행(objects) 전체(all) 조회하기
    # Select mem_id, mem_pass, mem_name, mem_add1 From member Where mem_id='a001'
    # objects.get() 값의 형태 = {"mem_id":"a001", "mem_pass":"asdf1234"...}
    mem_view = Member.objects.get(mem_id = mem_id)
    return render(request,
                  "oracleapp/member/mem_update_view.html",
                  {"mem_id" : mem_id,
                   "mem_view" : mem_view})
    
### 회원정보 상세 조회하기
def getMemberView(request):
    mem_id = request.GET.get("mem_id")
    
    ### Member 클래스에서 행(objects) 전체(all) 조회하기
    # Select mem_id, mem_pass, mem_name, mem_add1 From member Where mem_id='a001'
    # objects.get() 값의 형태 = {"mem_id":"a001", "mem_pass":"asdf1234"...}
    mem_view = Member.objects.get(mem_id = mem_id)
    return render(request,
                  "oracleapp/member/mem_view.html",
                  {"mem_id" : mem_id,
                   "mem_view" : mem_view})
    
### 회원정보 전체 행 조회하기
def getMemberList(request):
    ### Member 클래스에서 행(objects) 전체(all) 조회하기
    # Select mem_id, mem_pass, mem_name, mem_add1 From member
    # objects.all() 값의 형태 = [{"mem_id":"a001", "mem_pass":"asdf1234"...}, {}, {}]
    mem_list = Member.objects.all().order_by("mem_id")
    return render(request,
                  "oracleapp/member/mem_list.html",
                  {"mem_list" : mem_list})

### oracleapp 최초 페이지 처리
def index(request):
    ## return HttpResponse("OKOK.....")
    return render(request,
                  "oracleapp/index.html",
                  {})