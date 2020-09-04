from django import forms
from .models import Blog


#정상적으로 models.py 에 있는 모델을 참조 할경우
class BlogPost1(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','body']



# 아래 예제는 모델에 없는 경우의 입력 값을 마련한다.
class BlogPost2(forms.Form):
    email = forms.EmailField()
    files = forms.FileField()
    url = forms.URLField()
    words = forms.CharField(max_length=200)
    max_number = forms.ChoiceField(choices=[{'0' , 'zero'},{'1','one'},{'2','two'}])