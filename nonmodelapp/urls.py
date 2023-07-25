from django.urls import path

### firstapp 폴더 하위에 있는 views.py 파일 읽어들이기
# - 라이브러리 읽어들이는 것과 동일
from . import views
urlpatterns = [
    # - http://127.0.0.1:8000/nonmodel/index/
    path('index/', views.index),
    # - http://127.0.0.1:8000/nonmodel/index/
    path('about/', views.about),
    # - http://127.0.0.1:8000/nonmodel/index/
    path('contact/', views.contact),
    # - http://127.0.0.1:8000/nonmodel/index/
    path('doctor/', views.doctor),
    # - http://127.0.0.1:8000/nonmodel/index/
    path('testimonial/', views.testimonial),
    # - http://127.0.0.1:8000/nonmodel/index/
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
