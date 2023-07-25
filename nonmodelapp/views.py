from django.shortcuts import render
from django.http import HttpResponse
from .DB_Sql import disease
from .DB_Sql import sign_in
from .DB_Sql import user
from .DB_Sql import recom
from django.core.paginator import Paginator
from .models import Users, Userdis, Prod, Disease


def index(request):
    return render(request,
                  "nonmodelapp/index.html",
                  {})

def about(request):
    return render(request,
                  "nonmodelapp/about.html",
                  {})
    
def contact(request):
    return render(request,
                  "nonmodelapp/contact.html",
                  {})

def doctor(request):
    return render(request,
                  "nonmodelapp/doctor.html",
                  {})
    
def testimonial(request):
    return render(request,
                  "nonmodelapp/testimonial.html",
                  {})

def treatment(request):
    return render(request,
                  "nonmodelapp/treatment.html",
                  {})