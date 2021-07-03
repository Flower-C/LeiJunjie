from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from flower.models import Department

def show(request):
    dep=Department.objects
    for i in dep.all():
        print(i)
    return HttpResponse('1212')



def hello(request):

    return HttpResponse("Hello world ! ")