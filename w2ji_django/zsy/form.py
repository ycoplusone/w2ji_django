# 장고의 기본적으로 제공하는 품을 불러 옵니다.
from django import forms
# 폼을 통해 데이터를 추가하거나 수정할 post 모델을 로드
from .models import UserInfo

# 클래스 생성 forms.modelfrom 을 상속 받는다.
class UserInfoForm(forms.ModelForm):    
    # 이 폼에서 다룰 내용을 기술한다.
    class Meta:
        model = UserInfo
        fields = ('company_id' , 'user_id' ,'user_ps' ,'user_nm')
        widgets = {
            'company_id' : forms.Select( attrs={'class':'easyui-combobox' }) ,
            'user_id' : forms.TextInput(attrs={'class': 'easyui-textbox', 'label':'Name:' , 'iconCls':'icon-man'}),
            'user_ps' : forms.TextInput(attrs={'class': 'easyui-textbox', 'autocomplete':'off'}),
            'user_nm' : forms.TextInput(attrs={'class': 'easyui-textbox', 'autocomplete':'off'}),            
        }
        labels={
            'company_id' : '' ,
            'user_id' : '',
            'user_ps' : '',
            'user_nm' : '',
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