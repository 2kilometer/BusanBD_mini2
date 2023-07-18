from django.urls import path

### firstapp 폴더 하위에 있는 views.py 파일 읽어들이기
# - 라이브러리 읽어들이는 것과 동일
from . import views

### 사용자가 요청할 수 있는 URL을 정의합니다.
# - url 하나당, views의 함수 한개를 호출할 수 있도록 매핑합니다.
# - url을 정의한다고 해서, 패턴(pattern)정의라고 합니다.
urlpatterns = [
    ### 클라이언트(User)가 웹브라우저 URL창에 아래 주소 입력하면 index 호출
    
    ###############실습######################
    # - http://127.0.0.1:8000/oracle/cart_mem_prod_list/
    path('product/', views.getProduct),
    
    # - http://127.0.0.1:8000/oracle/cart_mem_prod_list/
    path('product_insert/', views.setProductInsert),
    
    
    
    
    
    
    
    
    
    ##### [주문 + 회원정보 + 상품정보 관리]
    # - http://127.0.0.1:8000/oracle/cart_mem_prod_list/
    path('cart_mem_prod_list/', views.getCartMemProdList),
    
    
    ##### [주문 + 회원정보 관리]
    # - http://127.0.0.1:8000/oracle/cart_mem_list/
    path('cart_mem_list/', views.getCartMemList),
    
    
    ##### [상품정보 관리]
    # - http://127.0.0.1:8000/oracle/prod_update/
    path('prod_update/', views.setProdUpdate),
    # - http://127.0.0.1:8000/oracle/prod_update_view/
    path('prod_update_view/', views.getProdUpdateView),
    # - http://127.0.0.1:8000/oracle/prod_view/
    path('prod_view/', views.getProdView),
    # - http://127.0.0.1:8000/oracle/prod_list/
    path('prod_list/', views.getProdList),
    
    ##### [상품분류정보 관리]
    # - http://127.0.0.1:8000/oracle/lprod_insert/
    path('lprod_insert/', views.setLprodInsert),
    # - http://127.0.0.1:8000/oracle/lprod_insert_view/
    path('lprod_insert_view/', views.getLprodInsertView),
    # - http://127.0.0.1:8000/oracle/lprod_update/
    path('lprod_update/', views.setLprodUpdate),
    # - http://127.0.0.1:8000/oracle/lprod_update_view/
    path('lprod_update_view/', views.getLprodUpdateView),
    # - http://127.0.0.1:8000/oracle/lprod_delete/
    path('lprod_delete/', views.setLprodDelete),
    # - http://127.0.0.1:8000/oracle/lprod_view/
    path('lprod_view/', views.getLprodView),
    # - http://127.0.0.1:8000/oracle/lprod_list/
    path('lprod_list/', views.getLprodList),
    
    ##### [주문정보 관리]
    # - http://127.0.0.1:8000/oracle/cart_insert/
    path('cart_insert/', views.setCartInsert),
    # - http://127.0.0.1:8000/oracle/cart_insert_view/
    path('cart_insert_view/', views.getCartInsertView),
    # - http://127.0.0.1:8000/oracle/cart_update/
    path('cart_update/', views.setCartUpdate),
    # - http://127.0.0.1:8000/oracle/cart_update_view/
    path('cart_update_view/', views.getCartUpdateView),
    # - http://127.0.0.1:8000/oracle/cart_delete/
    path('cart_delete/', views.setCartDelete),
    # - http://127.0.0.1:8000/oracle/cart_view/
    path('cart_view/', views.getCartView),
    # - http://127.0.0.1:8000/oracle/cart_list/
    path('cart_list/', views.getCartList),
        
    
    ##### [회원정보 관리]
    # - http://127.0.0.1:8000/oracle/mem_update/
    path('mem_update/', views.setMemberUpdate),
    # - http://127.0.0.1:8000/oracle/mem_update_view/
    path('mem_update_view/', views.getMemberUpdateView),
    # - http://127.0.0.1:8000/oracle/mem_view/
    path('mem_view/', views.getMemberView),
    # - http://127.0.0.1:8000/oracle/mem_list/
    path('mem_list/', views.getMemberList),
    
    # - http://127.0.0.1:8000/oracle/index/
    path('index/', views.index),
    # - http://127.0.0.1:8000/oracle/
    path('', views.index),
    # - http://127.0.0.1:8000/oracle/index.html
    path('index.html/', views.index),
]
