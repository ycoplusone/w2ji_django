from django.shortcuts import render , get_object_or_404, redirect
from aiohttp.client import request
from .models import Blog
from django.utils import timezone


# Create your views here.

def home(request):
    blog = Blog.objects
    return render(request , '_home.html',{'blogs':blog})

def detail(request , blog_id):
    #blog = Blog.objects
    #return render(request , '_detail.html',{'blogs':blog})
    blog_detail = get_object_or_404(Blog , pk=blog_id)
    return render(request , '_detail.html' , {'blog':blog_detail})

def new(request):
    if request.method == 'POST':
        blog = Blog()
        blog.title = request.POST['title']
        blog.body = request.POST['body']
        blog.pub_date = timezone.datetime.now()
        blog.save()
        return redirect('/test')
    else :
        return render(request , '_new.html')
    