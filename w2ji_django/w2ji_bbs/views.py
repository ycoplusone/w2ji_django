from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotAllowed, Http404
from django.views.generic import TemplateView
from . import models

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
            'detail' : bbs  
        }
        return self.render_to_response(ctx)
    

class cu_bbs(TemplateView): #생성및 수정, 수정시 글의 id 참조
    template_name = 'base.html'
    queryset = models.bbs.objects.all()
    pk_url_kwargs = 'bbs_id'
    
    def get_object(self, queryset=None):
        queryset = queryset or self.queryset
        pk = self.kwargs.get(self.pk_url_kwargs)
        bbs = queryset.filter(pk=pk).first()
        
        if pk and not bbs: #결과가 없다면 바로 에러 발생
            raise Http404('invalid pk')
        return bbs
    
    
    def get(self, request, *args, **kwargs): #화면 요청
        bbs = self.get_object()
        ctx = {
            'view' : self.__class__.__name__ , 
            'data' : bbs
        }
        return self.render_to_response(ctx)
    
    def post(self, request, *args, **kwargs): #액션
        action  = request.POST.get('action') #request.POST 객체에서 데이터 얻기
        post_data = {key:request.POST.get(key) for key in ('title','content','author')}
        for key in post_data:
            if not post_data[key]:
                raise Http404('no data for {}'.format(key))
        
        if action == 'create': #action이 create일 경우
            bbs = models.bbs.objects.create(title = post_data['title'] , content = post_data['content'] , author = post_data['author'])
        elif action == 'update': # action이 update일 경우
            bbs = self.get_object()
            if not bbs:
                raise Http404('invalid article_id')
            
            for key , value in post_data.items():
                setattr(bbs , key , value)
            
            bbs.save()
        else:
            raise Http404('invalid action')
                
        ctx = {
            'view' : self.__class__.__name__ , 
            'data' : bbs 
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