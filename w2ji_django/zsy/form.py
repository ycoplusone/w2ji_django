# 장고의 기본적으로 제공하는 품을 불러 옵니다.
from django import forms
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from .models import UserModel

# 폼을 통해 데이터를 추가하거나 수정할 post 모델을 로드
class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Email',
            'required': 'True',
        }
    ))
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password',
                'required': 'True',
            }
        )
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password confirmation',
                'required': 'True',
            }
        ),
        help_text="Enter the same password as above, for verification."
    )

    class Meta: # SignupForm에 대한 기술서
        model = UserModel
        fields = ("email", "password1", "password2",) # 작성한 필드만큼 화면에 보여짐


class LoginForm(AuthenticationForm):
    email = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'nickname',
                'required': 'True',
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password',
                'required': 'True',
            }
        )
    ) 



'''from .models import UserInfo

# 클래스 생성 forms.modelfrom 을 상속 받는다.
class UserSignupForm(forms.ModelForm):    
    # 이 폼에서 다룰 내용을 기술한다.
    class Meta:
        model = UserInfo
        fields = ('company_id' , 'user_id' ,'user_nm' , 'user_ps'  )
        widgets = {
            'company_id' : forms.Select( attrs={'class':'easyui-combobox', 'label':'회사선택' , 'style':'width: 280px;' , 'labelWidth':'100' , 'editable': 'false' }) ,
            'user_id'    : forms.TextInput(attrs={'class':'easyui-textbox', 'autocomplete':'off', 'label':'아 이 디' , 'style':'width: 280px;' , 'labelWidth':'100' }),            
            'user_nm'    : forms.TextInput(attrs={'class': 'easyui-textbox', 'autocomplete':'off' ,'label':'이    름' , 'style':'width: 280px;' , 'labelWidth':'100'}),
            'user_ps'    : forms.TextInput(attrs={'type':'password','class':'easyui-textbox', 'autocomplete':'off', 'label':'비밀번호' , 'style':'width: 280px;' , 'labelWidth':'100' }),
        }
        labels={
            'company_id' : '' ,
            'user_id' : '',            
            'user_nm' : '',
            'user_ps' : '',
        }


class UserLoginFrom(forms.ModelForm):        
    class Meta:
        model = UserInfo
        fields = ('company_id' , 'user_id' ,'user_ps')
        widgets = {
            'company_id' : forms.TextInput(attrs={'class':'easyui-textbox', 'autocomplete':'off', 'label':'회사코드' , 'style':'width: 300px;' }) ,
            'user_id'    : forms.TextInput(attrs={'class':'easyui-textbox', 'autocomplete':'off', 'label':'아 이 디' , 'style':'width: 300px;' }),
            'user_ps'    : forms.TextInput(attrs={'class':'easyui-textbox', 'autocomplete':'off', 'label':'비밀번호' , 'style':'width: 300px;' }),           
        }
        labels={
            'company_id' : '' ,
            'user_id' : '',
            'user_ps' : '',
        }
'''        