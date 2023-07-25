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
]
