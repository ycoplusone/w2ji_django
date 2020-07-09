from django.test import TestCase

from blog.models import Post

a = Post.objects.all()

print(a)
print('*'*50)
from django.contrib.auth.models import User
b = User.objects.all()
admin  = User.objects.get( username='admin' )

print(b)
print('*'*50)
print(admin )

# 데이터 insert 방법
Post.objects.create(author=admin, title='This is a test title from django shell', content='This is a test title from django shell. This is a test title from django shell.')

a = Post.objects.all()
print('*'*50)
print(a)


#데이터 update 방법
print('#데이터 update 방법')
post = Post.objects.get(id=2)
print(post)
post.title = 'fuck off herefff'
post.save()

print('*'*50)
a = Post.objects.get(id=2)
a.publish()
print(a)

print('#데이터 delete 방법')
post = Post.objects.get(title__contains='fuck')
print(post)
a = Post.objects.all()
print(a)
post.delete()
a = Post.objects.all()
print(a)

