from django.urls import path 
from . import views
from django.contrib.auth.views import LogoutView

app_name = "w2ji_user"
urlpatterns = [        
    path('create/'            , views.UserRegistrationView.as_view() ) , #회원가입
    path('login/'             , views.UserLoginView.as_view() ) , #로그인
    path('logout/'            , LogoutView.as_view() ) , #로그아웃
            
]