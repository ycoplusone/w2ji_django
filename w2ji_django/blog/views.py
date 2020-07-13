from django.shortcuts import render, get_object_or_404 , redirect
from django.utils import timezone
from .form import PostCreateForm

# Post 클래스를 로드한다.
from .models import Post 

def posts(request):
    # _isnull=False : not null 데이터 가저온다.    , order_by : 정렬을 한다.
    #cont = Post.objects.filter(published_at__isnull=True).order_by('-published_at')
    cont = Post.objects.all().order_by('-published_at')
    print( 'query \n', cont.query ) 
    return render( request , 'blog/posts.html' , { 'posts' : cont } ) # 1. 뷰 생성

def post_detail(request , id):
    cont = get_object_or_404(Post , id=id)
    return render( request , 'blog/post_detail.html' , { 'post' : cont } ) # 1. 뷰 생성

def post_create(request):
    if request.method == "POST":
        print('request',request)
        print('request.POST',request.POST)
        form = PostCreateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_at = timezone.now()            
            post.save()
            
            
            return redirect('post_detail', id=post.id)
    else:
        form = PostCreateForm()
    return render(request, 'blog/post_create.html', {'form': form})    