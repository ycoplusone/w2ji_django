from django.contrib import admin
from django.urls import include , path 
from django.conf import settings
from django.conf.urls.static import static

#Add URL maps to redirect the base URL to our application
from django.views.generic import RedirectView




urlpatterns = [
    #path(''   , admin.site.urls    ) ,    # 기본 default 페이지는 둔다.
    path('admin/'   , admin.site.urls),

    # 테스트 라인
    path('test/'     , include('test_song.urls') , name='test' ) , 
    
    # 시스템 관련 => 회원 , 권한 , 게시판 기능
    #path('zsy/'     , include('zsy.urls') , name='zsy') ,
    
    # 카탈로그 연결
    path('catalog/', include('catalog.urls') ), 
    
    path('', RedirectView.as_view(url='/catalog/', permanent=True)), # '' 로 접슥할시 catalog/로 넘긴다.
    
        
    
]+static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)

#if settings.DEBUG:
    #print('settings',settings)
    #urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   
