from django.shortcuts import render , redirect
from django.views import View
from django.http import JsonResponse, HttpResponse, Http404
from django.contrib.auth.models import User
from django.contrib import auth
from aiohttp.client import request

#from .form import UserSignupForm , UserLoginFrom

#from .models import UserInfo

def index(request):
    return HttpResponse('zsy index')

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
            auth.login(request, user)
            return redirect('home')
        return render(request , 'login/_signup.html')
    
    return render(request , 'login/_signup.html',)


def login(request):
    print( request.method )
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print('username : ',username,'password : ' , password)
        user = auth.authenticate(request , username=username , password = password)        
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request , 'login/_login.html',{'error':'your username or password incorrect'})
    else:
        return render(request , 'login/_login.html') 
    
    

def logout(request):
    auth.logout(request)
    return redirect('home')    

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