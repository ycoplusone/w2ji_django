from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField('date published')
    body = models.TextField()
    def __str__(self):
        return self.title
    def summary(self):
        return self.body[:30]

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    photo = models.ImageField(blank=True , upload_to='image/')    
    class Meta:
        db_table = 'test_post' # 테이블 이름 지정
    