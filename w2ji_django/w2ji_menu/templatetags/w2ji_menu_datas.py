from django import template

from .. import models

register = template.Library()

@register.simple_tag
def getGroup():
    datas = models.group.objects.all()
    return datas 

@register.simple_tag
def getMenu():
    datas = models.menu.objects.filter(use_yn='1')
    return datas
