"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

### include : 각 앱에서 관리하는 urls.py 호출 시 사용
from django.urls import path, include

### firstapp 폴더 하위에 있는 views.py 파일 읽어들이기
# - 라이브러리 읽어들이는 것과 동일

### 아래는 사용 안함(각 앱에서 처리하게 했음)
from mainapp import views as views3

### 사용자가 요청할 수 있는 URL을 정의합니다.
# - url 하나당, views의 함수 한개를 호출할 수 있도록 매핑합니다.
# - url을 정의한다고 해서, 패턴(pattern)정의라고 합니다.
urlpatterns = [
    ### 클라이언트(User)가 웹브라우저 URL창에 아래 주소 입력하면 index 호출
    
    ### http://127.0.0.1:8000/first/index1/
    # - 기본 URL 뒤에 있는 첫번째 이름과 두번째 이름 분리
    # - 첫번째 이름을 이용해서 각 앱을 찾아가게끔 설정
    # - 각 앱에서는 두번째 이름을 받아서 함수를 호출하게 함
    # - include() : 원하는 파일의 코드를 읽어들일 때 사용됨
    #             : include가 실행되는 순간
    #               해당 파일의 코드에서 처리가 됨
    path('', include('mainapp.urls')),
    path('nonmodel/', include('nonmodelapp.urls')),
    
    
    
    
    path('admin/', admin.site.urls),
]
