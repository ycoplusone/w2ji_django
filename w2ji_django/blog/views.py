from django.shortcuts import render

def posts(request):
    return render(request , 'blog/posts.html', {}) # 1. 뷰 생성