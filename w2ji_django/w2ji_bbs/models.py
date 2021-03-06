# w2ji_bbs : 게시판
from django.db import models


class bbs(models.Model):
    title = models.CharField('제목' , max_length = 126 , null = False)
    content = models.TextField('내용' , null = False )
    #author = models.CharField('작성자' , max_length = 16 , null = False)
    author = models.ForeignKey('w2ji_user.User' , related_name='bbs', on_delete=models.CASCADE)
    create_dt = models.DateTimeField('작성일', auto_now_add = True)
    #create_dt.editable = True
    update_dt = models.DateTimeField('수정일' , auto_now = True )
    #update_dt.editable = True #수정 가능 여부 

    
    
    class Meta:
        db_table = 'w2ji_bbs' # 테이블 이름 지정
    
    def __str__(self):
        return '[{}] {}'.format(self.id , self.title)