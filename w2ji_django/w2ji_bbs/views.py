from django.shortcuts import render
from django.http.response import HttpResponse



def hello(request,to):
    return HttpResponse('hello world {}'.format(to))