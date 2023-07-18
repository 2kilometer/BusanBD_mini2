from django.urls import path

### firstapp 폴더 하위에 있는 views.py 파일 읽어들이기
# - 라이브러리 읽어들이는 것과 동일
from . import views

### 사용자가 요청할 수 있는 URL을 정의합니다.
# - url 하나당, views의 함수 한개를 호출할 수 있도록 매핑합니다.
# - url을 정의한다고 해서, 패턴(pattern)정의라고 합니다.
urlpatterns = [
    ### 클라이언트(User)가 웹브라우저 URL창에 아래 주소 입력하면 index 호출
    
    ############# [Front-End : extends] ############     
    
    # - http://127.0.0.1:8000/front/35_hello /
    path('35_hello/', views.extendHello),
    
    # - http://127.0.0.1:8000/front/34_extend_layout /
    path('34_extend_layout/', views.extendLayoutView),
    
    
    ############# [Front-End : Include] ############   
    
    # - http://127.0.0.1:8000/front/33_main_index /
    path('33_main_index/', views.mainIndexView),
    
    # - http://127.0.0.1:8000/front/32_include_index /
    path('32_include_index/', views.includeIndexView), 
    
    
    ############# [Front-End : Bootstrap] ############  
    
    # - http://127.0.0.1:8000/front/31_bootstrap_layout /
    path('31_bootstrap_layout/', views.bootstrapLayoutView), 
    
    # - http://127.0.0.1:8000/front/30_bootstrap_form /
    path('30_bootstrap_form/', views.bootstrapFormView), 
    
    # - http://127.0.0.1:8000/front/29_bootstrap_table /
    path('29_bootstrap_table/', views.bootstrapTableView), 
    
    # - http://127.0.0.1:8000/front/28_bootstrap /
    path('28_bootstrap/', views.bootstrapView),
    
    
    
    ############# [Front-End : Javascript] ############   
    
    # - http://127.0.0.1:8000/front/26_selectbox /
    path('27_selectbox2/', views.selectBoxView2),
    # - http://127.0.0.1:8000/front/26_selectbox /
    path('26_selectbox/', views.selectBoxView),
    
    # - http://127.0.0.1:8000/front/24_checkbox /
    path('25_checkbox2/', views.checkBoxView2),
    # - http://127.0.0.1:8000/front/24_checkbox /
    path('24_checkbox/', views.checkBoxView),
    
    # - http://127.0.0.1:8000/front/21_radio/
    path('23_radio2/', views.jsRadio2),
    # - http://127.0.0.1:8000/front/20_radioButton/
    path('22_radioButton2/', views.radioButtonView2),
    
    # - http://127.0.0.1:8000/front/21_radio/
    path('21_radio/', views.jsRadio),
    # - http://127.0.0.1:8000/front/20_radioButton/
    path('20_radioButton/', views.radioButtonView),
    
    # - http://127.0.0.1:8000/front/19_login/
    path('19_login/', views.jsLogin),
    
    # - http://127.0.0.1:8000/front/18_jsInputForm/
    path('18_jsInputForm/', views.jsInputFormView),
    
    
    
    
    ############# [Front-End : CSS] ############ 
    
    # - http://127.0.0.1:8000/front/17_cssNav/
    path('17_cssNav/', views.cssNavView),
    
    # - http://127.0.0.1:8000/front/16_cssTable/
    path('16_cssTable/', views.cssTableView2),
    
    # - http://127.0.0.1:8000/front/15_cssTable/
    path('15_cssTable/', views.cssTableView),



    ############# [Front-End : HTML] ############ 
    
    # - http://127.0.0.1:8000/front/14_iframe/
    path('14_iframe/', views.iframeView),
    
    # - http://127.0.0.1:8000/front/13_div/
    path('13_div/', views.divView2),
    
    # - http://127.0.0.1:8000/front/12_div/
    path('12_div/', views.divView),
    
    # - http://127.0.0.1:8000/front/11_ul/
    path('11_ul/', views.ulView),
    
    # - http://127.0.0.1:8000/front/10_mem_list/
    path('10_mem_list/', views.mem_List),
    
    # - http://127.0.0.1:8000/front/09_mem/
    path('09_mem/', views.mem_View),
    
    # - http://127.0.0.1:8000/front/08_table/
    path('08_table/', views.tableView02),
    
    # - http://127.0.0.1:8000/front/07_table/
    path('07_table/', views.tableView),
    
    # - http://127.0.0.1:8000/front/06_css/
    path('06_css/', views.cssView06),
    
    # - http://127.0.0.1:8000/front/05_css/
    path('05_css/', views.cssView05),
    
    # - http://127.0.0.1:8000/front/04_css/
    path('04_css/', views.cssView04),
    
    # - http://127.0.0.1:8000/front/03_css/
    path('03_css/', views.cssView),
    
    # - http://127.0.0.1:8000/front/02_link/
    path('02_link/', views.linkView),
    
    # - http://127.0.0.1:8000/front/01_html/
    path('01_html/', views.htmlVeiw01),
    
    # - http://127.0.0.1:8000/front/
    path('', views.index),
]
