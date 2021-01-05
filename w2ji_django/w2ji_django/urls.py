from django.contrib import admin
from django.urls import include , path 
from django.conf import settings
from django.conf.urls.static import static

#Add URL maps to redirect the base URL to our application
from django.views.generic import RedirectView
from w2ji_bbs.views import hello




urlpatterns = [
    path('test/'     , include('test_song.urls') , name='test' ) ,# 테스트 라인
    #path(''   , admin.site.urls    ) ,    # 기본 default 페이지는 둔다.
    path('admin/'   , admin.site.urls),
        
   
    path('w2ji_tiny/'           , include('w2ji_tinydash.urls')  ) , # tinydash UI 테스트  
    
    path('w2ji_bbs/'            , include('w2ji_bbs.urls')  ) , # 게시판 앱
    path('w2ji_user/'           , include('w2ji_user.urls')  ) , # 사용자 
    
    
    #path('', RedirectView.as_view(url='/catalog/', permanent=True)), # '' 로 접슥할시 catalog/로 넘긴다.
    
]+static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)

#if settings.DEBUG:
    #print('settings',settings)
    #urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   
