from django.shortcuts import render
from django.views.generic.base import TemplateView
from . import models

'''
    queryset = None #models.bbs.objects.all() #모든 게시글을 가져온다.
    
    def get(self, request, *args, **kwargs):
        ctx = { 
            'view' : self.__class__.__name__ , #클래스의 이름
            'data' : menu.objects.all() ,    #self.queryset #걸색결과 
        }    #템플릿에 전달할 데이터
        return self.render_to_response(ctx)
'''


class menu(TemplateView):
    template_name = 'menu.html' #뷰 전용 템플릿 생성    
    queryset = models.menu.objects.all()
    
    def get(self, request, *args, **kwargs):
        ctx = { 
            'view' : self.__class__.__name__ , #클래스의 이름
            'datas' : self.queryset ,    #self.queryset #걸색결과 
        }    #템플릿에 전달할 데이터
        return self.render_to_response(ctx)
