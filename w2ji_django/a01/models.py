from django.db import models

class q(models.Model):
    q_t = models.CharField(max_length=200)
    p_d = models.DateTimeField('date published')
    
    def __str__(self):
        return self.q_t
    
    class Meta:
        db_table ='a01_question'
        
class c(models.Model):
    q = models.ForeignKey(q, on_delete=models.CASCADE)
    c_t = models.CharField(max_length=200)
    v = models.IntegerField(default=0)
    
    def __str__(self):
        return self.c_t
        
    class Meta:
        db_table ='a01_choice'                