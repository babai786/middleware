from django.shortcuts import render
from django.http  import  HttpResponse
# Create your views here.


def welcome(request):
    print('this is printed by view')
    return HttpResponse('<h3> COSTOM MIDDLEWARE</h3>')
