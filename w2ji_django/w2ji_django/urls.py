from django.contrib import admin
from django.urls import include , path 
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    #path(''   , admin.site.urls    ) ,    # 기본 default 페이지는 둔다.
    path('admin/'   , admin.site.urls),
    
    #path(''   , include('blog.urls')    ), # 기본 url 정보가 오면 blog.urls 로 라우팅한다.
    
    #path(''         , include('zsy.urls')   ) ,    # 기본 default 페이지는 둔다.
    
    #테스트 라인
    path('test/'     , include('test_song.urls') , name='test' ) , 
    # 테스트 라인
    path('zsy/'     , include('zsy.urls') , name='zsy') ,
    
        
    
]+static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
'''
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
'''   
