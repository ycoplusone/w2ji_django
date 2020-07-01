from django.db import models

class User(models.Model):
    user_id     = models.CharField( max_length =20 , verbose_name = '아이디' , help_text = '아이디를 입력하세요' )    # 아이디
    email       = models.CharField( max_length =100, verbose_name = '이메일' , help_text = '이메일 주소를 입력하세요' )    # 이메일
    user_ps     = models.CharField( max_length =50 , verbose_name = '비밀번호' , help_text = '비밀번호를 입력하세요' )    # 비밀번호
    user_nm     = models.CharField( max_length =50 , verbose_name = '이름' , help_text = '이름를 입력하세요' )   # 이름
    user_hp     = models.CharField( max_length =50 , verbose_name = '휴대폰' , help_text = '휴대 전화번호를 입력하세요' )   # 휴대폰
    user_tel    = models.CharField( max_length =50 , verbose_name = '연락처' , help_text = '연락처를 입력하세요' )   # 연락처
    access_dt = models.DateTimeField( auto_now_add=True, blank=True) # 마지막 접속일자
    create_dt = models.DateTimeField( auto_now_add = True) # 생성일 : 레코드 생성시 자동 생성
    update_dt = models.DateTimeField( auto_now = True) # 수정일 : 레코드 수정시 
    
    # db 테이블 이름을 정할수 있다.
    class Meta:
        db_table ='system_user'