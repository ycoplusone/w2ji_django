from django.shortcuts import render , redirect
from django.views import View
from django.http import JsonResponse, HttpResponse, Http404
#from django.contrib.auth.models import User
from .models import UserModel

from django.contrib import auth
from aiohttp.client import request
from django.contrib.auth.decorators import login_required

from .form import SignupForm , LoginForm

#from .models import UserInfo

@login_required
def index(request):
    return render(request , 'login/_index.html')

def signup(request):
    form = SignupForm()
    if request.method == 'POST':        
        if request.POST['password1'] == request.POST['password2']:            
            user = UserModel.objects.create_user(email=request.POST['email'], password=request.POST['password1'])
            auth.login(request, user)
            return redirect('zsy:index')
        else:
            return render(request , 'login/_signup.html' , {'form':form})
    else:
        return render(request , 'login/_signup.html' , {'form':form})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #print('username : ',username,'password : ' , password)
        user = auth.authenticate(request , username=username , password = password)  
        if user is not None:
            auth.login(request, user)
            return redirect('zsy:index')
        else:
            return render(request , 'login/_login.html',{'error':'your username or password incorrect'})
    else:
        return render(request , 'login/_login.html') 
    
    

def logout(request):
    auth.logout(request)
    return redirect('zsy:index')    

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