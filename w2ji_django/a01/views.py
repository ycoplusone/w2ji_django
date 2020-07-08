from django.shortcuts import render
from django.http import HttpResponse
import random
from .models import q

def index(req):
    return HttpResponse( 'a01 index : '+ str( random.random() ))
    

def detail(req , q_id):
    return HttpResponse("You're looking at question %s." % q_id)

def result(req , q_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % q_id)

def vote(req,q_id):
    return HttpResponse("You're voting on question %s." % q_id)