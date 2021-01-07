from django.shortcuts import render
from django.views.generic.base import TemplateView


class index(TemplateView):  #목록보기
    template_name = 'index.html' #뷰 전용 템플릿 생성
    queryset = None #models.bbs.objects.all() #모든 게시글을 가져온다.
    
    def get(self, request, *args, **kwargs):
        ctx = { 
            'view' : self.__class__.__name__ , #클래스의 이름
            #'lists' : self.get_queryset() ,    #self.queryset #걸색결과 
        }    #템플릿에 전달할 데이터
        return self.render_to_response(ctx)

class uicolor(TemplateView):
    template_name = 'ui-color.html' #뷰 전용 템플릿 생성

class uitypograpy(TemplateView):
    template_name = 'ui-typograpy.html' #뷰 전용 템플릿 생성

class uiicons(TemplateView):
    template_name = 'ui-icons.html' #뷰 전용 템플릿 생성

class uibuttons(TemplateView):
    template_name = 'ui-buttons.html' #뷰 전용 템플릿 생성

class uinotification(TemplateView):
    template_name = 'ui-notification.html' #뷰 전용 템플릿 생성

class uimodals(TemplateView):
    template_name = 'ui-modals.html' #뷰 전용 템플릿 생성

class uitabsaccordion(TemplateView):
    template_name = 'ui-tabs-accordion.html' #뷰 전용 템플릿 생성

class uiprogress(TemplateView):
    template_name = 'ui-progress.html' #뷰 전용 템플릿 생성
        
