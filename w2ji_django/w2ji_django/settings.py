"""
Django settings for w2ji_django project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from django.conf.global_settings import AUTH_USER_MODEL, LOGOUT_REDIRECT_URL
from django.urls import reverse_lazy

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'vkmrmmqzo^5$#zfry5vbn+u6*l7$)cllp-5d+%bp#-9l@@iy-$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True # 테스트 일경우 true , 실서버 배포시 false

ALLOWED_HOSTS = []
AUTH_USER_MODEL = 'w2ji_user.User' #앱label.모델명 2020.12.28 추가
LOGIN_REDIRECT_URL = '/w2ji_bbs/'  # 로그인이 되면 /article/로 이동
LOGIN_URL = '/w2ji_user/login/' #로그인 url

# Application definition
INSTALLED_APPS = [
    
    'django.contrib.admin',             # 관리자용 사이트
    'django.contrib.auth',              # 인증 시스템
    'django.contrib.contenttypes',      # 다양한 종류의 모델 데이터를 관리할수 있게 도와주는 앱
    'django.contrib.sessions',          # 클라이언트 정보를 세션에서 관리하도록 하는 프레임워크
    'django.contrib.messages',          # 컨트롤러에서 발생한 정보를 뷰에서 쉽게 접근하도록 연결하는 프레임워크
    'django.contrib.staticfiles',       # HTML, CSS , JS 파일등의 정적파일들을 관리해주는 프레임워크
    
    'test_song.apps.TestSongConfig', #테스트 객체    
    
    'w2ji_bbs.apps.W2JiBbsConfig',#게시판 앱 추가
    'w2ji_user.apps.W2JiUserConfig',# 사용자인증
    'w2ji_tinydash.apps.W2JiTinydashConfig',# tinydash Ui 테스트
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware', #사용자인증 관한 처리 auth_login 통해 세션관리
    'django.contrib.auth.middleware.AuthenticationMiddleware', #사용자인증 관한 처리 
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',    
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'w2ji_django.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR , "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]



WSGI_APPLICATION = 'w2ji_django.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    
    
    'default' : {
        'ENGINE'  : 'django.db.backends.mysql'  , # 엔진 설정
        'NAME'    : 'w2ji_django'               , # db스키마      
        'USER'    : 'w2ji_django'               , # db 계정            
        'PASSWORD': 'w2ji_django'               , # db 비밀번호     
        'HOST'    : 'localhost'                 , # 서버 정보
        'PORT'    : '3306'                      , # 서버 포트
        'OPTIONS' : {
            'init_command': 'SET sql_mode="STRICT_TRANS_TABLES"'
        }        
    } ,    
    
    'test_sqlite3': {
        'ENGINE'  : 'django.db.backends.sqlite3'            ,
        'NAME'    : os.path.join(BASE_DIR, 'w2ji.sqlite3')    ,
    } ,
        
    
     
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'ko-kr'
#LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True
USE_L10N = True
USE_TZ = True #기본시간대(UTC)에 대해서 사용 유무를 선택함.


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR , 'static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR , 'media')

