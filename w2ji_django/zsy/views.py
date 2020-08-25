from django.shortcuts import render , redirect
import json
from django.views import View
from django.http import JsonResponse, HttpResponse, Http404

#from .form import UserSignupForm , UserLoginFrom

#from .models import UserInfo

def signup():
    return HttpResponse('signup')

def login():
    return HttpResponse('login')

def logout():
    return HttpResponse('logout')    

'''
class LoginView(View):
    def post(self,request):
        data = json.loads(request.body)
'''

'''
def signup(request):
    form = UserSignupForm()
    if request.method =='POST':
        print( request.POST['user_ps'] )
        print( request.POST['user_ps2'] )
        if request.POST['user_ps'] == request.POST['user_ps2']:
            print('맞아')
        else:
            print('틀려')
    else:
        return render(request, 'login/_signup.html', {'form': form , 'title':'Login - System'})
'''        
    
    
    
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

'''
def login(request):
    form = UserLoginFrom()
    return render(request, 'login/_login.html', {'form': form , 'title':'Login - System'})

def logout(request):
    form = UserLoginFrom()
    return render(request, 'login/_login.html', {'form': form , 'title':'Login - System'})
'''