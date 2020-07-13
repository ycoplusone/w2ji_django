# 장고의 기본적으로 제공하는 품을 불러 옵니다.
from django import forms
# 폼을 통해 데이터를 추가하거나 수정할 post 모델을 로드
from .models import Post

# 클래스 생성 forms.modelfrom 을 상속 받는다.
class PostCreateForm(forms.ModelForm):
    
    # 이 폼에서 다룰 내용을 기술한다.
    class Meta:
        model = Post
        fields = ('content' , 'title')