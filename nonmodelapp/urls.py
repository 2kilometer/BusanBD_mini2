from django.urls import path

### firstapp 폴더 하위에 있는 views.py 파일 읽어들이기
# - 라이브러리 읽어들이는 것과 동일
from . import views

### 사용자가 요청할 수 있는 URL을 정의합니다.
# - url 하나당, views의 함수 한개를 호출할 수 있도록 매핑합니다.
# - url을 정의한다고 해서, 패턴(pattern)정의라고 합니다.
urlpatterns = [
    # - http://127.0.0.1:8000/nonmodel/temptreat/
    path('temptreat/', views.tempTreatView),
    # - http://127.0.0.1:8000/nonmodel/temptesti/
    path('temptesti/', views.tempTestiView),
    # - http://127.0.0.1:8000/nonmodel/tempabout/
    path('tempabout/', views.tempAboutView),
    # - http://127.0.0.1:8000/nonmodel/tempcont/
    path('tempcont/', views.tempContView),
    # - http://127.0.0.1:8000/nonmodel/tempdoct/
    path('tempdoct/', views.tempDoctView),
    # - http://127.0.0.1:8000/nonmodel/tempindex/
    path('tempindex/', views.tempIndexView)
]
