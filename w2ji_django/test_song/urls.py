from django.urls import path 
from . import views


urlpatterns = [
    path('' , views.home , name = 'index' ) , 
    path('<int:blog_id>', views.detail , name = 'detail' ) ,
    path('new/' , views.new , name = 'new'),
        
        
    
]
