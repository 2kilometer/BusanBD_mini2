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




