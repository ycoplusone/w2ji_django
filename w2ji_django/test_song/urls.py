from django.urls import path 
from . import views

app_name = "test_song"
urlpatterns = [
    path('' , views.home , name = 'index' ) ,   #테스트 기본 페이지  리스트가 나온다.
    path('detail/<int:blog_id>', views.detail , name = 'detail' ) , # 상세 페이지
    path('new/' , views.new , name = 'new'), # 신규 글 작성
    path('new2/' , views.new2 , name = 'new2'), # 신규 글 작성
    
    path('detail/<int:blog_id>/delete' , views.delete , name = 'delete' ) , # 삭제
    path('detail/<int:blog_id>/edit'   , views.edit   , name = 'edit' ) , # 수정

    
]
