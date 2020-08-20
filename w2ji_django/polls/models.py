from django.db import models


class Question(models.Model):
    question_text = models.CharField( max_length=200 )
    update_dt = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text+' : '+self.update_dt
    
    class Meta:
        db_table = 'polls_question' # 테이블 이름 지정


class Choice(models.Model):
    question = models.ForeignKey(Question , on_delete=models.CASCADE)
    choice_text = models.CharField( max_length=200 )
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.question+' : '+self.choice_text+' : '+self.votes
    
    class Meta:
        db_table = 'polls_choice' # 테이블 이름 지정