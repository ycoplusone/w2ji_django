from django.db import models

class group(models.Model):
    '''메뉴 그룹'''
    group_nm = models.CharField('그룹명' , max_length = 126, null = False) #그룹명이 없으면 단독 실행
    group_icon = models.CharField('아이콘' , max_length = 126, null = True )
    group_sort = models.IntegerField('그룹순서')
    create_dt = models.DateTimeField('작성일', auto_now_add = True)
    update_dt = models.DateTimeField('수정일' , auto_now = True )
    class Meta:
        db_table = 'w2ji_menu_group' # 테이블 이름 지정
    
    def __str__(self):
        return '{} [{}]'.format( self.group_nm , self.group_sort )

class menu(models.Model):
    '''메뉴 리스트'''
    group = models.ForeignKey('w2ji_menu.group' , on_delete=models.CASCADE , null=True )
    #author = models.ForeignKey('w2ji_user.User' , related_name='bbs', on_delete=models.CASCADE)
    menu_nm  = models.CharField('메뉴명' , max_length = 126 , null = False)
    menu_url = models.CharField('메뉴 링크' , max_length = 256 , null = False)    
    menu_descript = models.TextField('메뉴 설명' , null = True )
    menu_sort = models.IntegerField('메뉴순서')    
    use_yn = models.BooleanField('사용여부' , null = True)
    create_dt = models.DateTimeField('작성일', auto_now_add = True)
    update_dt = models.DateTimeField('수정일' , auto_now = True )    
    
    class Meta:
        db_table = 'w2ji_menu' # 테이블 이름 지정
    
    
    def __str__(self):
        return '{} - {} - {}'.format(self.id , self.group ,self.menu_nm )
    