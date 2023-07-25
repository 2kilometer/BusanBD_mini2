from django.shortcuts import render
from django.http import HttpResponse

from nonmodelapp.nonmodel import cart, member

### 페이징처리 라이브러리
from django.core.paginator import Paginator

### 파일 업/다운로드 라이브러리
from nonmodelapp.file_util.file_util import File_Util

### 데이터시각화를 이미지로 저장하는 라이브러리
from nonmodelapp.data_view.data_view import Data_View

### 지도맵 시각화를 처리하는 라이브러리
from nonmodelapp.map_view.map_view import Map_View

# Create your views here.
def tempTreatView (request) :
    return render (request,
                   "nonmodelapp/temp/treatment.html",
                   {})
     
def tempTestiView (request) :
    return render (request,
                   "nonmodelapp/temp/testimonial.html",
                   {})
    
def tempAboutView (request) :
    return render (request,
                   "nonmodelapp/temp/about.html",
                   {})
     
def tempContView (request) :
    return render (request,
                   "nonmodelapp/temp/contact.html",
                   {})
     
def tempDoctView (request) :
    return render (request,
                   "nonmodelapp/temp/doctor.html",
                   {})
     
def tempIndexView(request) :
    return render (request,
                   "nonmodelapp/temp/index.html",
                   {})

##############jquery##########################
def load_view(request):
     return render(request,
                  "nonmodelapp/jquery_load/load_view.html",
                  )
     
     
def load_view1(request):
     return render(request,
                  "nonmodelapp/jquery_load/load_view1.html",
                  )


def load_view2(request):
     return render(request,
                  "nonmodelapp/jquery_load/load_view2.html",
                  )
     
def load_view3(request):
     return render(request,
                  "nonmodelapp/jquery_load/load_view3.html",
                  )









############### 지도맵 시각화 웹에서 표현하기 #############
def map_Visualization(request) :
    ### 클래스 생성시키기
    # - 생성자가 자동 호출되어 지도를 그려줍니다.
    #   (__init__() 함수 자동호출)
    map_view = Map_View()
    
    ### 지도맵 시각화 HTML로 받아오기
    map_html = map_view.getMap()
    
    ### 지도맵 시각화에 사용된 데이터프레임 받아오기
    # - to_html()로 처리한 html 내부는 컨트롤이 불가능함
    # - 데이터프레임을 스타일 등 적용해서 원하는 모양으로 만들기 위해서는
    #   -> 리스트의 딕셔너리 형태 [{},{},{}]로 만들어서 사용하면 됩니다.
    #   -> table 태그를 사용해서 컨트롤 가능합니다.
    map_data = map_view.getDataFrame()
    
    return render(request,
                  "nonmodelapp/map_view/map_view.html",
                  {"map_html" : map_html,
                   "map_data" : map_data.to_html()})
    

############### 데이터 시각화 이미지를 웹에서 표현하기 #############
def data_Visualization(request) :
    data_view = Data_View()
    return render(request,
                  "nonmodelapp/data_view/data_view.html",
                  {})
    

############### 파일 업로드 / 다운로드 처리하기 #############
### 파일 다운로드 처리
def setDownload(request) :
    download_full_name = request.GET.get("download_full_name", "")
    
    fu = File_Util()
    
    ### 다운로드에 필요한 값 설정하기
    fu.setDownload(download_full_name)
        
    # return HttpResponse(download_full_name)
    ### 실제 파일 다운로드하기
    return fu.fileDownload()
    

### 파일 업로드 처리
def getFileUpload(request) :
    # 제목 받기
    title = request.POST.get("title", "")
    # 파일 받기
    # - file을 받을 때는 FILES 딕션너리 변수 사용..
    file_nm = request.FILES.get("file_nm", "")
    
    msg = "{} / {}".format(title, file_nm)
    
    ### 파일 업로드를 위한 물리적 위치 설정하기
    # - 물리적인 파일 업로드 위치 지정하기
    upload_dir = "./nonmodelapp/static/nonmodelapp/file_UpDown/" 
    # - 물리적인 다운로드 위치 지정하기
    download_dir = "./nonmodelapp/static/nonmodelapp/file_UpDown/" 
    # - 물리적인 이미지 경로 지정하기(이미지 파일인 경우)
    img_dir = "/static/nonmodelapp/file_UpDown/"
    
    ### 파일 업로드 및 다운로드에 사용할 클래스 만들기
    fu = File_Util()
    
    ### 파일 업로드시 -> 최초에 초기값 셋팅하기
    fu.setUpload(file_nm, upload_dir, img_dir, download_dir)
    
    ### 실제로 파일 업로드 시키기
    fu.fileUpload()
    
    ### 업로드된 파일 정보 조회하기  ###
    # 파일 사이즈
    file_size = fu.file_size
    # 업로드된 파일명
    filename = fu.filename
    # 이미지인 경우 : 이미지 src 경로에 넣을 경로+파일명
    img_full_name = fu.img_full_name
    # 다운로드인 경우 : 다운로드 경로 + 파일명
    download_full_name = fu.download_full_name
    
    ### DB를 이용해서 업로드된 정보를 테이블에 저장하고자 할 경우
    # - 사용할 컬럼은 img_full_name과 download_full_name만 저장해 놓으면 됨
    
    ### HTML 작성하기
    msg = """
            <p>img_full_name : {0}</p>
            <p>file_size : {1}</p>
            <p>filename : {2}</p>
            <p>다운로드 파일명 : 
                <a href='/nonmodel/file_down/?download_full_name={3}'>{2}</a>
            </p>
            <p>이미지 파일인 경우 :
                <img src='{0}'>
            </p>
    """.format(img_full_name, file_size, filename, download_full_name)
    
    return HttpResponse(msg)
    
### 파일 업로드 페이지 처리
def getFileUploadForm(request) :
    return render(request,
                  "nonmodelapp/file_upload/file_upload_form.html",
                  {})
    
    

############### 로그인/로그아웃 처리하기 #############
### 로그인 처리 
def login_chk(request) :
    # - 아이디 및 패스워드 전송받기
    mem_id = request.POST.get("mem_id", "")
    mem_pass = request.POST.get("mem_pass", "")
    
    mem_view = member.getLoginChk(mem_id, mem_pass)
    
    ### mem_view의 결과값 중 key (result)의 값이 None면
    # - 회원정보가 일치하기 않습니다. 다시입력해 주세요! 라는
    # - 메시지 보여주고, index 페이지로 다시 보내기
    if mem_view.get("result") == "None" :
        msg = """
            <script type='text/javascript'>
                alert('회원정보가 일치하기 않습니다. 다시입력해 주세요!');
                location.href = '/front/login/';
            </script>
        """
        return HttpResponse(msg)
    
    msg = "{} / {} / {}".format(mem_view["mem_id"], 
                                mem_view["mem_pass"],
                                mem_view["mem_name"])
    
    ### 로그인 인증처리하기 (세션처리하기)
    # - 조회결과가 있으면 세션객체에 회원정보를 담으면 끝~
    # - 세션객체는 딕셔너리 타입 입니다.
    # - 세션객체에 값을 담는것은 딕셔너리에 값을 넣는것과 동일함
    request.session["ses_mem_id"] = mem_id
    request.session["ses_mem_name"] = mem_view.get("mem_name")
    
    ### 로그인 인증처리(세션처리) 후 페이지 링크 처리
    msg = """
            <script type='text/javascript'>
                alert('환영합니다. [{}]님 로그인 되었습니다.');
                location.href = '/';
            </script>
    """.format(mem_view.get("mem_name"))
    
    return HttpResponse(msg)

### 로그아웃 처리
def logout_chk(request) :
    msg = "logout ok...."
    
    ### 로그아웃 처리는 session 딕셔너리의 key를 없애주면 됩니다.
    # - 딕셔너리에서 모든 정보 삭제하는 함수 :flush()
    request.session.flush()
    
    msg = """
          <script type='text/javascript'>
            alert('로그아웃 되었습니다!');
            location.href = '/';
          </script>
    """
    
    return HttpResponse(msg)


################ 페이징(paging) 처리하기
def getCartListPaging(request):
    
    ########### paging - 초기 변수값 처리 시작 ############
    ### 현재 페이지 번호 설정
    now_page = request.GET.get("page", "1")
    
    # 전송되는 모든 데이터 타입은 문자열 
    # - now_page 값은 숫자로 사용 : 숫자형태로 형변환 시켜야 합니다.
    now_page = int(now_page)    
    #### paging 처리 끝....
    
    cart_list = cart.cart_List()
    
    ########### paging - 목록 데이터 처리 시작 ############
    ### 한 화면에 10개 행씩 보여주기 위해 
    #   - 조회한 결과에서 10개 추출하기
    ### 한 화면에 보여줄 행의 갯수 지정
    num_row = 10
    
    ### Paginator() : 행의 갯수만큼 데이터 추출하는 라이브러리
    p = Paginator(cart_list, num_row)
    
    ### 현제 페이지번호에 대항하는 10개 데이터 추출하기
    # - 최초 now_page는 1 입니다.
    # - Paginator가 10개 행씩 가지고 있는 순서 중 1번째 그룹을 추출
    rows_data = p.get_page(now_page)
    #### paging 처리 끝....
    
    
    ########### paging - 하단 페이지 처리 시작 ############
    ### 시작페이지 번호(start_page) 계산하기
    start_page = (now_page - 1) // num_row * num_row + 1
    
    ### 종료페이지 번호(end_page) 계산하기
    end_page = start_page + 9
    
    ### 종료페이지의 번호가 전체 행의 갯수보다 크면...
    # p.num_page : 전체 행의 갯수
    if end_page > p.num_pages :  
        end_page = p.num_pages  
    #### paging 처리 끝....
    
    ########### paging - 다음/이전 버튼 처리 시작 ############
    ### 다음/이전 버튼을 보여줄지 여부에 대한 체크 변수
    # - 이전버튼 체크를 위한 초기값
    is_prev = False
    # - 다음버튼 체크를 위한 초기값
    is_next = False
    
    ### 이전버튼 보여줄지 여부 처리
    if start_page > 1 :
        is_prev = True
    
    ### 다음버튼 보여줄지 여부 처리
    if end_page < p.num_pages :
        is_next = True
    #### paging 처리 끝....
    
    context = {
        ### 데이터 목록 리스트
        "cart_list" : rows_data,
        ### 현재 페이지 번호 : 현재 선택된 값을 유지하기 위해서 사용
        "now_page" : now_page,
        ### 이전버튼 처리 변수
        "is_prev" : is_prev,
        ### 다음버튼 처리 변수
        "is_next" : is_next,
        ### 시작페이지 번호
        "start_page" : start_page,
        ### 페이지번호의 시작(start_page) ~ 종료페이지(end_page) 범위
        "page_range" : range(start_page, end_page + 1)
    }
    
    return render(request,
                  "nonmodelapp/paging/cart_list.html",
                  context)
    

################ nonmodelapp 최초 페이지 처리
def index(request):
    return render(request,
                  "nonmodelapp/index.html",
                  {})