from django.shortcuts import render
from .DB_Sql import disease

# Create your views here.

# mainapp에서 최초 호출 함수로 사용..


def index(request):
    return render(request,
                  "mainapp/index.html",
                  {})


def Register(request):
    age = request.POST.get("age", "")
    dis_list = disease.dis_list()
    dis_middle = disease.dis_middle()
    if age != "":
        dis_age = disease.dis_age(age)
    else:
        dis_age = disease.dis_age('10대')
    return render(request,
                  "mainapp/register.html",
                  {"dis_list" : dis_list,
                   "dis_middle" : dis_middle,
                   "dis_age" : dis_age,})

def Register1(request) :    
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
