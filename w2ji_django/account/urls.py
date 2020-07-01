from django.urls import path , include
from .views import SignInView , SignUpView

#app_name ='polls'   # 앱의 네임 스페이스
urlpatterns = [
    path('up',SignUpView.as_view()) ,
    path('in',SignInView.as_view()) , 
]
