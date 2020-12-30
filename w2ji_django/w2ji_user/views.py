from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import get_user_model

from .forms import UserRegistrationForm , LoginForm
from django.contrib import messages



class UserRegistrationView(CreateView):
    '''
    - 회원 가입 부분
    CreateView를 상속 받으면
    model 과 fields 만 구현한다.
    CreateView변수에서는 자동으로 해당앱의 templates 디렉토리에서 앱 이름의 디렉토리 하위의 모델 명_form.html 파일을 템플릿으로 사용
    ex) user_  
    
    '''
    template_name ='user_model.html'
    #model = User                            # 자동생성 폼에서 사용할 모델
    form_class = UserRegistrationForm #UserCreationForm   #가입품을 처음부터 만들어야 하나 했지만  usercreationform 클래스를 이용하면 쉽다.
    #fields = ('email', 'name', 'password')  # 자동생성 폼에서 사용할 필드 form_class 사용시에는 필요 없다.
    success_url = '/w2ji_bbs/'
    
class UserLoginView(LoginView):           # 로그인
    authentication_form = LoginForm
    template_name = 'login_form.html'

    def form_invalid(self, form):
        messages.error(self.request, '로그인에 실패하였습니다.', extra_tags='danger')
        return super().form_invalid(form)        
    