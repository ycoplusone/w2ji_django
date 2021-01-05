from django.urls import path 
from . import views

app_name = 'w2ji_tinydash'
urlpatterns = [    
    
    #path('hello/<to>'       , views.hello ) ,
    path(''             , views.index.as_view()  ) ,
    
    
]