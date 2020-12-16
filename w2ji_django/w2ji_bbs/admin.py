from django.contrib import admin
from .models import bbs


@admin.site.register(bbs)
class bbsAdmin(admin.ModelAdmin):
    list_display = ('id','title','content') #date_updated 아래 정의한 메소드
    list_display_links = ('id','title') #상세페이지로 이동할수 있는 필드 리스트
    '''
    def date_updated(self , obj):
        return obj.update_dt.strftime("%Y-%m-%d")

    date_updated.admin_order_field = 'update_dt'             # date_created 컬럼 제목을 클릭시 실제 어떤 데이터를 기준으로 정렬할 지 결정
    date_updated.short_description = '작성일'                   # date_created 컬럼 제목에 보일 텍스트
    '''