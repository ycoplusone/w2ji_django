from django.urls import path 
from . import views

app_name = 'w2ji_menu'
urlpatterns = [    
    path('' , views.menu.as_view()     ) , 
    path('jsontest/' , views.jsontest     ) ,
    
]
