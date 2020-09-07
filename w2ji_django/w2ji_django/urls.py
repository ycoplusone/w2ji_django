from django.contrib import admin
from django.urls import include , path 
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    #path(''   , admin.site.urls    ) ,    # 기본 default 페이지는 둔다.
    path('admin/'   , admin.site.urls),

    # 테스트 라인
    path('test/'     , include('test_song.urls') , name='test' ) , 
    
    # 시스템 관련 => 회원 , 권한 , 게시판 기능
    path('zsy/'     , include('zsy.urls') , name='zsy') ,
    
        
    
]+static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)

#if settings.DEBUG:
    #print('settings',settings)
    #urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   
