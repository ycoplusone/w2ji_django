from django.db import models


class chart(models.Model):
    
    dt      = models.CharField('일자' , max_length = 126, null = False) #그룹명이 없으면 단독 실행
    mon     = models.CharField('년월' , max_length = 126, null = True) #그룹명이 없으면 단독 실행
    sale    = models.IntegerField('판매금액')
    amount  = models.IntegerField('수량')
    cost    = models.IntegerField('단가')
    
    
    class Meta:        
        db_table = 'w2ji_chart' # 테이블 이름 지정
        
    
    def __str__(self):
        return '{} - {} - {} - {}'.format( self.dt , self.sale , self.amount , self.cost )



        
            