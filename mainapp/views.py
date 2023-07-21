from django.shortcuts import render

# Create your views here.

# mainapp에서 최초 호출 함수로 사용..


def index(request):
    return render(request,
                  "mainapp/index.html",
                  {})


def Register(request):
    return render(request,
                  "mainapp/register.html",
                  {})
    
def Data_info(request):
    return render(request,
                  "mainapp/data_info.html",
                  {})

def Recom(request):
    return render(request,
                  "mainapp/recom.html",
                  {})

def Statistic(request):
    return render(request,
                  "mainapp/statistic.html",
                  {})
