import json
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .models import Account

class SignUpView(View):
    def post(self , req):
        data = json.load(req.body)
        print('SignUpView post data',data)
        Account(
            user_id = data['user_id'] ,
            #user_ps = data['user_ps'] ,
            #email   = data['email'] ,
            #user_nm = data['user_nm'] ,
            #user_hp = data['user_hp'] ,
            #user_tel = data['user_tel'] ,
        ).save() # db에 저장한다.
        
        return JsonResponse({'message':'회원가입 완료'},status=200)

class SignInView(View):
    def post(self , req):
        data = json.load(req.body)
        
        if Account.objects.filter(user_id = data['user_id']).exists() :
            user = Account.objects.get(user_id = data['user_id'])
            if user.user_ps == data['user_ps'] :
                return JsonResponse({'message':f'{user.user_nm}님 로그인 성공!'}, status=200)
            else :
                return JsonResponse({'message':'비밀번호가 틀렸어요'},status = 200)

        return JsonResponse({'message':'등록되지 않은 이메일 입니다.'},status=200)
        
        
        
        
        
        
        
        