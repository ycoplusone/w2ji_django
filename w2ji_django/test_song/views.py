from django.shortcuts import render , get_object_or_404, redirect
from aiohttp.client import request
from .models import Blog
from django.utils import timezone
from django.core.paginator import Paginator
from .form import BlogPost

from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def home(request):
    blog = Blog.objects
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list , 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request , '_home.html',{'blogs':blog , 'posts':posts})

def detail(request , blog_id):

    blog_detail = get_object_or_404(Blog , pk=blog_id)
    return render(request , '_detail.html' , {'blog':blog_detail})

def new(request):
    if request.method == 'POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.datetime.now()
            post.save()
            '''
            blog = Blog()
            blog.title = request.POST['title']
            blog.body = request.POST['body']
            blog.pub_date = timezone.datetime.now()
            blog.save()
            '''
        return redirect('test_song:index')
    else :
        form = BlogPost()
        return render(request , '_new.html' , {'form':form})

def delete(request ,blog_id ):
    blog = Blog.objects.get(id=blog_id)
    blog.delete()
    return redirect('test_song:index')

'''
def edit(request, blog_id):
    cat = Cat.objects.get(id=blog_id)
    # 글을 수정사항을 입력하고 제출을 눌렀을 때
    if request.method == "POST":
        form = CatPost(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            # {'name': '수정된 이름', 'image': <InMemoryUploadedFile: Birman_43.jpg     (image/jpeg)>, 'gender': 'female', 'body': '수정된 내용'}
            cat.name = form.cleaned_data['name']
            cat.image = form.cleaned_data['image']
            cat.gender = form.cleaned_data['gender']
            cat.body = form.cleaned_data['body']
            cat.save()
            return redirect('/detail/'+str(cat.pk))
        
    # 수정사항을 입력하기 위해 페이지에 처음 접속했을 때
    else:
        form = CatPost()
        return render(request, 'postapp/edit_post.html',{'form':form})
'''    