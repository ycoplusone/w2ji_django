from django.shortcuts import render
from django.core import serializers
from django.http.response import HttpResponse
import json


from django.db.models import functions as fn
from django.db import models as db
import numpy as np

from rest_framework import viewsets
from . import models 
from dataclasses import field



def chartjson(request):
    
    queryset = models.chart.objects.values('dt','mon').annotate(
    sale=db.Sum('sale')
    ).filter(
    db.Q(dt__startswith='202101')
    )    
    
    
    print('jsontest',queryset.query)
    print(queryset)    
    
    
    res = json.dumps(list(queryset))
    
    return HttpResponse(res, content_type="text/json-comment-filtered")

def chart2json(request):
    data = [{'name': 'Peter', 'email': 'peter@example.org'},
            {'name': 'Julia', 'email': 'julia@example.org'}]

    #return JsonResponse(data, safe=False)
    return HttpResponse(data, content_type="text/json-comment-filtered")

def chart3json(request):
    datas = models.chart.objects.values('mon').annotate(
        sale=db.Sum('sale')
        ,amount=db.Sum('amount')
    ).filter()
    print(datas.query)
    res = json.dumps(list(datas))
    return HttpResponse(res, content_type="text/json-comment-filtered") 
    
       
