from django.urls import path , include
from . import views

#app_name ='polls'   # 앱의 네임 스페이스
urlpatterns = [
    path('', views.index , name='index') ,
    
    path('<int:q_id>/', views.detail , name='detail') ,
    
    path('<int:q_id>/results',views.result , name='result') ,
    
    path('<int:q_id>/vote',views.vote , name='vote') ,
     
]
