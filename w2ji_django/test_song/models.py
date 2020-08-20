from django.db import models

class test_1(models.Model):
    question_text = models.CharField( max_length=200 )
    update_dt = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text+' : '+self.update_dt
    
    class Meta:
        db_table = 'test_question' # 테이블 이름 지정


class test_2(models.Model):
    
    choice_text = models.CharField( max_length=200 )
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text+' : '+self.votes
    
    class Meta:
        db_table = 'test_choice' # 테이블 이름 지정