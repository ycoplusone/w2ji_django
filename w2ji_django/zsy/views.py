from django.shortcuts import render , redirect
import json
from django.views import View
from django.http import JsonResponse
from .form import UserInfoForm , UserLoginFrom

from .models import UserInfo

class LoginView(View):
    def post(self,request):
        data = json.loads(request.body)



def create(request):
    form = UserInfoForm()
    return render(request, 'login/_login.html', {'form': form})
    '''
    if request.method=='POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/feedback/list')
    else:
        form = UserInfoForm()

    return render(request, 'feedback.html', {'form': form})
    ''' 
def LoginFrom(request):
    form = UserLoginFrom()
    return render(request, 'login/_login.html', {'form': form , 'title':'Login - System'})
