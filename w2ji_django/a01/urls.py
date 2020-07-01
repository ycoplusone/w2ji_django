from django.urls import path , include
from .views import index

#app_name ='polls'   # 앱의 네임 스페이스
urlpatterns = [
    path('',index) ,
     
]
