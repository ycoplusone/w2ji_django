from django.db import models

class CompanyInfo(models.Model):
    company_id  = models.CharField( max_length =20 , verbose_name = '회사코드' , primary_key = True)
    company_nm  = models.CharField( max_length =40 , verbose_name = '회사명' ) 
    use_yn      = models.CharField( max_length =1  ,default ='y' , verbose_name = '사용유무') #사용유무 y:사용 , n:미사용
    update_dt   = models.DateTimeField( auto_now_add=True, blank=True) # 최근접속일
    def __str__(self):
        return self.company_nm+'('+self.company_id+')'
    class Meta:
        db_table = 'zsy_company_info' # 테이블 이름 지정
        unique_together = (('company_id'),) #기본키 설정

class UserInfo(models.Model):
    company_id  = models.ForeignKey( CompanyInfo    ,  on_delete=models.CASCADE)
    #group_id    = models.ForeignKey( GroupInfo      ,  on_delete=models.CASCADE)
    #dept_id     = models.ForeignKey( DeptInfo       ,  on_delete=models.CASCADE)
    user_id     = models.CharField( max_length =20   )    # 아이디
    user_ps     = models.CharField( max_length =50   )    # 비밀번호
    user_nm     = models.CharField( max_length =50 )
    email       = models.CharField( max_length =100 , verbose_name = '이메일' , blank=True )    # 이메일
    user_hp     = models.CharField( max_length =50 , verbose_name = '휴대폰'  , blank=True )   # 휴대폰
    user_tel    = models.CharField( max_length =50 , verbose_name = '연락처'  , blank=True )   # 연락처
    use_yn      = models.CharField( max_length =1  ,default ='y' , verbose_name = '사용유무') #사용유무 y:사용 , n:미사용
    access_dt   = models.DateTimeField( auto_now_add=True, blank=True) # 최근접속일
    update_dt   = models.DateTimeField( auto_now = True) # 수정일 : 레코드 수정시
    update_id   = models.CharField( max_length =20 , verbose_name = '수정 아이디'  , blank=True)
    
    def __str__(self):
        return self.user_nm+'('+self.user_id+')'
    
    class Meta:
        db_table = 'zsy_user_info' # 테이블 이름 지정
        unique_together = (('company_id', 'user_id'),) #기본키 설정
    