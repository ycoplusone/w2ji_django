from django.urls import path 
from . import views

app_name = "w2ji_bbs"
urlpatterns = [    
    
    #path('hello/<to>'       , views.hello ) ,    
    path(''             , views.bbs_list.as_view()) ,#글 목록
    path('detail/<bbs_id>/'     , views.bbs_detail.as_view() ) ,#상세보기
    path('create/'       , views.bbs_CreateUpdate.as_view() , {'bbs_id':None}) ,#글 생성 {'bbs_id':None} 필수
    path('update/<bbs_id>/',views.bbs_CreateUpdate.as_view() ) ,#글 수정
    
    
]