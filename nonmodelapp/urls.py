from django.urls import path

### firstapp 폴더 하위에 있는 views.py 파일 읽어들이기
# - 라이브러리 읽어들이는 것과 동일
from . import views
urlpatterns = [
    # - https://127.0.0.1:8000/nonmodel/temp/
    path('temp/', views.tempView),
    # - https://127.0.0.1:8000/nonmodel/login_chk/
    path('login_chk/', views.login_chk),
    # - https://127.0.0.1:8000/nonmodel/logout_chk/
    path('logout_chk/', views.logout_chk),
    # - http://127.0.0.1:8000/nonmodel/index/
    path('index/', views.index),
    # - http://127.0.0.1:8000/nonmodel/about/
    path('about/', views.about),
    # - http://127.0.0.1:8000/nonmodel/contact/
    path('contact/', views.contact),
    # - http://127.0.0.1:8000/nonmodel/doctor/
    path('doctor/', views.doctor),
    # - http://127.0.0.1:8000/nonmodel/login/
    path('login/', views.login),
    # - http://127.0.0.1:8000/nonmodel/treatment/
    path('treatment/', views.treatment),
    # - https://127.0.0.1:8000/register1/
    path('register1/', views.Register1),
    # - https://127.0.0.1:8000/register1/
    path('sign_in/', views.sign),
    # - https://127.0.0.1:8000/register1/
     path('recom_dis/', views.Recom_dis),
    # - https://127.0.0.1:8000//
    path('dis_add/', views.dis_add),
    # - https://127.0.0.1:8000//
    path('insert_view/', views.Insert_view),
    # - https://127.0.0.1:8000//
    path('insert_view2/', views.Insert_view2),
    # - https://127.0.0.1:8000//
    path('prodprod/', views.prodprod),
    # - https://127.0.0.1:8000//
    path('naver/', views.naver),
    # - https://127.0.0.1:8000//
]
