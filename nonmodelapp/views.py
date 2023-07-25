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
def TreatView (request) :
    return render (request,
                   "nonmodelapp/treatment.html",
                   {})
     
def TestiView (request) :
    return render (request,
                   "nonmodelapp/testimonial.html",
                   {})
    
def AboutView (request) :
    return render (request,
                   "nonmodelapp/about.html",
                   {})
     
def ContView (request) :
    return render (request,
                   "nonmodelapp/contact.html",
                   {})
     
def DoctView (request) :
    return render (request,
                   "nonmodelapp/doctor.html",
                   {})
     
def IndexView(request) :
    return render (request,
                   "nonmodelapp/index.html",
                   {})




