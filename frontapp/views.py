from django.shortcuts import render
from django.http import HttpResponse

from frontapp.DB_Sql import member

# Create your views here.
def index(requets):
    return render(requets,
                  "frontapp/index.html",
                  {})
    
############# [Front-End : extends] ############

### extendHello
def extendHello(request):
    return render(request,
                  "frontapp/extend/35_hello.html ",
                  {})    

### extendLayoutView
def extendLayoutView(request):
    return render(request,
                  "frontapp/extend/34_extend_layout.html ",
                  {})    
    
    
############# [Front-End : Include] ############

### mainIndexView
def mainIndexView(request):
    return render(request,
                  "frontapp/include/33_main_index.html",
                  {})      

### includeIndexView
def includeIndexView(request):
    return render(request,
                  "frontapp/include/32_include_index.html",
                  {})      
    
    
############# [Front-End : Bootstrap] ############

### bootstrapLayoutView() 
def bootstrapLayoutView(request):
    return render(request,
                  "frontapp/bootstrap/31_bootstrap_layout.html",
                  {})       

### bootstrapFormView 
def bootstrapFormView(request):
    return render(request,
                  "frontapp/bootstrap/30_bootstrap_form.html",
                  {})        

### bootstrapTableView 
def bootstrapTableView(request):
    return render(request,
                  "frontapp/bootstrap/29_bootstrap_table.html",
                  {})        

### bootstrapView 
def bootstrapView(request):
    return render(request,
                  "frontapp/bootstrap/28_bootstrap.html",
                  {})   
    
    
    
############# [Front-End : Javascript] ############     

### selectBoxView2 
def selectBoxView2(request):
    ### 딕셔너리 get은 문자열 데이터만 처리가능
    # - 리스트로 전송되는 데이터는 getlist()함수를 사용해야함
    if request.POST.get("mem_addr_one") is not None :
        mem_addr = request.POST.get("mem_addr_one")
        
    if request.POST.get("mem_addr_multi") is not None :
        ### getlist() : 파이썬의 리스트 형태로 데이터 받음
        #  - 예시 : ["서울", "부산"]
        mem_addr_list = request.POST.getlist("mem_addr_multi")
                
    return render(request,
                  "frontapp/js/27_selectbox.html",
                  {"mem_addr" : mem_addr,
                   "mem_addr_list" : mem_addr_list})  
    
### selectBoxView 
def selectBoxView(request):
    return render(request,
                  "frontapp/js/26_selectbox.html",
                  {})   

### checkBoxView2 
def checkBoxView2(request):
    ### 딕셔너리 get은 문자열 데이터만 처리가능
    # - 리스트로 전송되는 데이터는 getlist()함수를 사용해야함
    if request.POST.get("mem_addr") is not None :
        mem_addr = request.POST.get("mem_addr")
        ### getlist() : 파이썬의 리스트 형태로 데이터 받음
        #  - 예시 : ["서울", "부산"]
        mem_addr_list = request.POST.getlist("mem_addr")
        # str_list = "서울,대전";        
        
        str_list = ""
        for i in range(0, len(mem_addr_list)) :
            str_list += mem_addr_list[i]
            if i < len(mem_addr_list)-1 :
                str_list += ","
                
    return render(request,
                  "frontapp/js/25_checkbox.html",
                  {"mem_addr" : mem_addr,
                   "mem_addr_list" : mem_addr_list,
                   "str_list" : str_list})     
    
### checkBoxView 
def checkBoxView(request):
    return render(request,
                  "frontapp/js/24_checkbox.html",
                  {})  
    
    

### jsRadio2 수정 시 기존 데이터 보여지게 처리
def jsRadio2(request):
    try :
        ### 브라우저에서 요청한(입력한) 데이터 받아오기
        if request.method == "POST":
            if request.POST.get("mem_addr") is not None :
                mem_addr = request.POST["mem_addr"]
                mem_addr = request.POST.get("mem_addr")
                mem_addr1 = request.POST.get("mem_addr1")
            else :
                rsmsg = """
                    <script type='text/javascript'>
                        alert('잘못된 접근입니다.111');
                        history.go(-1);
                    </script>
                """       
                return HttpResponse(rsmsg)
            
        elif request.method == "GET":
            if request.GET.get("mem_addr") is not None :
                mem_addr = request.GET["mem_addr"]
                mem_addr = request.GET.get("mem_addr")
                mem_addr1 = request.GET.get("mem_addr1")
            else :
                rsmsg = """
                    <script type='text/javascript'>
                        alert('잘못된 접근입니다.333');
                        history.go(-1);
                    </script>
                """       
                return HttpResponse(rsmsg)
        
        ### 결과 처리 영역
        # 부산인지 아닌지 비교하기
        if mem_addr1 == "부산" :
            rsmsg = """
                    <script type='text/javascript'>
                        alert('{} 지역을 선택하셨습니다!!');
                        location.href='/front/';
                    </script>
            """.format(mem_addr1)
        else :
            rsmsg = """
                    <script type='text/javascript'>
                        alert('부산 지역이 아닙니다. 다시 선택해 주세요!');
                        history.go(-1);
                    </script>
            """.format(mem_addr1)
        
        ### 최종 결과 출력                    
        return HttpResponse(rsmsg)
     
    except :
        rsmsg = """
                    <script type='text/javascript'>
                        alert('잘못된 접근입니다.222');
                        history.go(-1);
                    </script>
                """
        return HttpResponse(rsmsg)  
    
    
### radioButtonView2 -> 수정인 경우 기존데이터 보여지게 처리
def radioButtonView2(request):
    return render(request,
                  "frontapp/js/22_radioButton2.html",
                  {"mem_addr" : "부산",
                   "mem_addr1" : "부산"})   
    
    

### jsRadio 처리
def jsRadio(request):
    try :
        ### 브라우저에서 요청한(입력한) 데이터 받아오기
        if request.method == "POST":
            if request.POST.get("mem_addr") is not None :
                mem_addr = request.POST["mem_addr"]
                mem_addr = request.POST.get("mem_addr")
                mem_addr1 = request.POST.get("mem_addr1")
            else :
                rsmsg = """
                    <script type='text/javascript'>
                        alert('잘못된 접근입니다.111');
                        history.go(-1);
                    </script>
                """       
                return HttpResponse(rsmsg)
            
        elif request.method == "GET":
            if request.GET.get("mem_addr") is not None :
                mem_addr = request.GET["mem_addr"]
                mem_addr = request.GET.get("mem_addr")
                mem_addr1 = request.GET.get("mem_addr1")
            else :
                rsmsg = """
                    <script type='text/javascript'>
                        alert('잘못된 접근입니다.333');
                        history.go(-1);
                    </script>
                """       
                return HttpResponse(rsmsg)
        
        ### 결과 처리 영역
        # 부산인지 아닌지 비교하기
        if mem_addr1 == "부산" :
            rsmsg = """
                    <script type='text/javascript'>
                        alert('{} 지역을 선택하셨습니다!!');
                        location.href='/front/';
                    </script>
            """.format(mem_addr1)
        else :
            rsmsg = """
                    <script type='text/javascript'>
                        alert('부산 지역이 아닙니다. 다시 선택해 주세요!');
                        history.go(-1);
                    </script>
            """.format(mem_addr1)
        
        ### 최종 결과 출력                    
        return HttpResponse(rsmsg)
     
    except :
        rsmsg = """
                    <script type='text/javascript'>
                        alert('잘못된 접근입니다.222');
                        history.go(-1);
                    </script>
                """
        return HttpResponse(rsmsg)  
    
    
### radioButtonView 처리
def radioButtonView(request):
    return render(request,
                  "frontapp/js/20_radioButton.html",
                  {})  
       
### jsLogin  처리
def jsLogin (request):
    rsmsg = "로그인 페이지 입니다."
    
    ### 요청 데이터 추출하기
    # post 방식
    # - request 변수가 모든 요청 정보를 가지고 있음
    # - method : 요청 시에 전송방식 확인
    # - 값을 추출하는 방식 : 딕셔너리 변수는 POST
    # - POST 딕셔너리 변수를 이용해서 파이썬 문법에 맞게 추출
    if request.method == "POST" :
        mem_id = request.POST["mem_id"]
        mem_pass = request.POST["mem_pass"]
    
    ### GET 방식으로 요청이 들어온 경우 아래 처리..
    elif request.method == "GET" :
        mem_id = request.GET["mem_id"]
        mem_pass = request.GET["mem_pass"]
        
    rsmsg = "아이디 : {} / 패스워드 : {}".format(mem_id, mem_pass)
    
    ### 요청받은(입력받은) 데이터와 비교하기 위한 기준 데이터 정의
    # - 실제로는 DB에 조회해서 결과 확인 후 있으면 정상, 없으면 비정상 처리
    p_id = 'b001'
    p_pw = '1357'
    
    ### 조건처리
    if (p_id == mem_id) & (p_pw == mem_pass) :
        rsmsg = "아이디 {}님 정상적으로 로그인 되었습니다".format(mem_id)
    else :
        rsmsg = "아이디 또는 패스워드를 확인해 주세요!"        
    
    ### 조건처리 : 자바스크립트로 응답해 주기
    if (p_id == mem_id) & (p_pw == mem_pass) :
        rsmsg = """
                <script type='text/javascript'>
                    alert('아이디 {}님 정상적으로 로그인 되었습니다');
                    location.href = '/front/';
                </script>
        """.format(mem_id)
    else :
        rsmsg = """
                <script type='text/javascript'>
                    alert('아이디 또는 패스워드를 확인해 주세요!');
                    history.go(-1);
                </script>
        """
    
    return HttpResponse(rsmsg) 
    
    
### jsInputFormView  처리
def jsInputFormView (request):
    mem_id = "b001"
    mem_pass = "1234"
    contexts = {"mem_id" : mem_id, 
                "mem_pass" : mem_pass}
    return render(request,
                  "frontapp/js/18_jsInputForm.html",
                  contexts)  

############# [Front-End : CSS] ############  
       
### cssTableView2 처리
def cssNavView(request):
    return render(request,
                  "frontapp/css/17_cssNav.html",
                  {})  
    
### cssTableView2 처리
def cssTableView2(request):
    return render(request,
                  "frontapp/css/16_cssTable.html",
                  {})  
       
### cssTableView 처리
def cssTableView(request):
    return render(request,
                  "frontapp/css/15_cssTable.html",
                  {})  
    
    
    

############# [Front-End : HTML] ############ 
       
### iframeView 처리
def iframeView(request):
    return render(request,
                  "frontapp/html/14_iframe.html",
                  {})  
       
### divView2 처리
def divView2(request):
    return render(request,
                  "frontapp/html/13_div.html",
                  {})  
       
### divView 처리
def divView(request):
    return render(request,
                  "frontapp/html/12_div.html",
                  {})  
       
### ulView 처리
def ulView(request):
    return render(request,
                  "frontapp/html/11_ul.html",
                  {})  
    
### DB > SQL 조회 결과 활용하기
def mem_List(request) :
    list_data = member.mem_List()
    return render(request,
                  "frontapp/html/10_mem_list.html",
                  {"list_data" : list_data})
    
### DB 활용하기
def mem_View(request) :
    msg = member.testData()
    return render(request,
                  "frontapp/html/09_mem.html",
                  {"msg" : msg})
    
### tableView 처리
def tableView02(request):
    # return render(request,
    #               "frontapp/html/08_table.html",
    #               {"mem_id":"a001",
    #                "mem_name":"홍길동",
    #                "mem_addr":"부산 수연구 수연동"}) 
    
    ### 테이블 기준으로 -> 딕셔너리 1개는 행 1개를 의미함...
    context = {"mem_id":"b001",
                "mem_name":"홍길동2",
                "mem_addr":"부산 수연구 수연동"} 
    
    mem_list = [context, context, context]    
    contexts = {"mem_list":mem_list,
                "mem_id":"b001",
                "mem_name":"홍길동2",
                "mem_addr":"부산 수연구 수연동"}
    
    ### render()함수의 3번째 인자값은 딕셔너리 타입만 가능합니다.
    return render(request,
                  "frontapp/html/08_table.html",
                  contexts)
    
### tableView 처리
def tableView(request):
    return render(request,
                  "frontapp/html/07_table.html",
                  {})    
    
### cssView 처리
def cssView06(request):
    return render(request,
                  "frontapp/html/06_css.html",
                  {})    
    
### cssView 처리
def cssView05(request):
    return render(request,
                  "frontapp/html/05_css.html",
                  {})    
    
### cssView 처리
def cssView04(request):
    return render(request,
                  "frontapp/html/04_css.html",
                  {})
    
### cssView 처리
def cssView(request):
    return render(request,
                  "frontapp/html/03_css.html",
                  {})
    
### linkView 처리
def linkView(request):
    return render(request,
                  "frontapp/html/02_link.html",
                  {})
    
### 01_html 처리
def htmlVeiw01(request):
    return render(request,
                  "frontapp/html/01_html.html",
                  {})