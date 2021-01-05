from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotAllowed, Http404,HttpResponseRedirect
from django.contrib import messages
from django.views.generic import TemplateView
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings

'''
    장고는 FBV와 CBV로 뷰를 개발할수 있다.
    FBV(FUNCTION BASED VIEW) 함수 즉 def 기반으로 개발한다.
    CBV(CLASS BASED VIEW) 즉 class 기반으로 개발한다.
'''


def hello(request,to):
    return HttpResponse('hello world {}'.format(to))

class bbs_list(TemplateView):  #목록보기
    template_name = 'bbs_list.html' #뷰 전용 템플릿 생성
    queryset = None #models.bbs.objects.all() #모든 게시글을 가져온다.
    
    def get(self, request, *args, **kwargs):
        ctx = { 
            'view' : self.__class__.__name__ , #클래스의 이름
            'lists' : self.get_queryset() ,    #self.queryset #걸색결과 
        }    #템플릿에 전달할 데이터
        return self.render_to_response(ctx)
    
    def get_queryset(self):
        if not self.queryset:
            self.queryset = models.bbs.objects.all()
        return self.queryset
        

class bbs_detail(TemplateView): #상세보기 , 글의 id 참조
    template_name = 'bbs_detail.html'
    queryset = models.bbs.objects.all()
    pk_url_kwargs = 'bbs_id' #검색데이터의 primary key 를 전달 받을 이름
    
    def get_object(self , queryset=None):
        queryset = queryset or self.queryset #queryset 파라미터 초기화
        pk = self.kwargs.get(self.pk_url_kwargs) #pk는 모델에서 정의된pk값, 즉 모델의 id
        bbs = queryset.filter(pk=pk).first()
        if not bbs:
            raise Http404('invalid pk')
        return bbs #pk로 검색된 데이터가 있다면 그 중 첫번째 데이터 없다면 None 반환
    
    def get(self, request, *args, **kwargs):
        bbs = self.get_object()
        '''
        if not bbs:
            raise Http404('invalid bbs_id') #검색된 데이터가 없다면 에러 발생
        '''
        ctx = {
            'view' : self.__class__.__name__ , 
            'data' : bbs  
        }
        return self.render_to_response(ctx)

class bbs_create(LoginRequiredMixin , TemplateView):
    login_url = settings.LOGIN_URL #설정값으로 설정
    template_name = 'bbs_update.html'    
    queryset = None #models.bbs.objects.all() #모든 게시글을 가져온다.
    
    def get(self, request, *args, **kwargs):
        ctx = { 
            'view' : self.__class__.__name__ , #클래스의 이름
            'lists' : self.get_queryset() ,    #self.queryset #걸색결과 
        }    #템플릿에 전달할 데이터
        return self.render_to_response(ctx)
    

class bbs_CreateUpdate(LoginRequiredMixin , TemplateView): #생성및 수정, 수정시 글의 id 참조    
    login_url = settings.LOGIN_URL
    template_name = 'bbs_update.html'
    queryset = models.bbs.objects.all()
    pk_url_kwargs = 'bbs_id'
    success_message = '게시글이 저장되었습니다.'
    
    def get_object(self, queryset=None):
        queryset = queryset or self.queryset
        pk = self.kwargs.get(self.pk_url_kwargs)
        bbs = queryset.filter(pk=pk).first()
        
        if pk and not bbs: #결과가 없다면 바로 에러 발생            
            raise Http404('invalid pk')
        return bbs
    
    
    def get(self, request, *args, **kwargs): #화면 요청
        ''''''
        bbs = self.get_object()
        ctx = {
            'view' : self.__class__.__name__ , 
            'data' : bbs
        }
        return self.render_to_response(ctx)
    
    def post(self, request, *args, **kwargs): #액션
        action  = request.POST.get('action') #request.POST 객체에서 데이터 얻기
        post_data = {key:request.POST.get(key) for key in ('title','content')}
        for key in post_data:
            if not post_data[key]:
                messages.error(self.request, '{} 값이 존재하지 않습니다.'.format(key), extra_tags='danger') # error 레벨로 메시지 저장
        
        post_data['author'] = self.request.user     
        
        if len(messages.get_messages(request)) == 0:                  # 메시지가 있다면 아무것도 처리하지 않음
            if action == 'create': #action이 create일 경우
                bbs = models.bbs.objects.create(**post_data)
                messages.success(self.request, self.success_message)  # success 레벨로 메시지 저장
            elif action == 'update': # action이 update일 경우
                bbs = self.get_object()                
                for key , value in post_data.items():
                    setattr(bbs , key , value)                
                bbs.save()
                messages.success(self.request, self.success_message)  # success 레벨로 메시지 저장
            else:
                messages.error(self.request, '알 수 없는 요청입니다.', extra_tags='danger')     # error 레벨로 메시지 저장
            
            return HttpResponseRedirect('/w2ji_bbs/') # 정상적인 저장이 완료되면 '/articles/'로 이동됨
                
        ctx = {
            'view' : self.__class__.__name__ , 
            'data' : self.get_object() if action == 'update' else None 
        }
        return self.render_to_response(ctx) 

    
    '''
    if bbs_id: #수정하기
        if request.method == 'GET':
            return HttpResponse('update {}'.format(bbs_id))
        elif request.method == 'POST':
            return do_create_bbs(request)
        else:
            return HttpResponseNotAllowed(['GET','POST'])
    else: #생성하기
        if request.method == 'GET':
            return HttpResponse('create')
        elif request.method == 'POST':
            return do_create_bbs(request)
        else :
            return HttpResponseNotAllowed(['GET','POST'])
    '''

def do_create_bbs(request):
    return HttpResponse(request.POST)

def do_update_bbs(request):
    return HttpResponse(request.POST)     