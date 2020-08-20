from django.contrib import admin

from .models import UserInfo,CompanyInfo

admin.site.register(UserInfo)
admin.site.register(CompanyInfo)