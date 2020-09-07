from django.urls import path 
from . import views

app_name = 'zsy'
urlpatterns = [
    path('' , views.index , name='index'      ), 
    path('signup/' , views.signup , name='signup'         ), #가입
    path('login/' , views.login  , name='login'         ), #로그인
    path('logout/' , views.logout , name='logout'        ), #로그아웃
    
    #path(''             , views.login   ),
    

    
    #path('post/<int:id>'   , views.post_detail , name = 'post_detail'),    
    #path('post/create'   , views.post_create , name = 'post_create'),
    
        
    
]
