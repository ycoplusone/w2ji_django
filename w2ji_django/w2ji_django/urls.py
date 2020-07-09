from django.contrib import admin
from django.urls import include , path 

urlpatterns = [
    path('admin/'   , admin.site.urls),
    
    path(''   , include('blog.urls')    ), # 기본 url 정보가 오면 blog.urls 로 라우팅한다.
        
    
]
