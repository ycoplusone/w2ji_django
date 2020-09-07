from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager,PermissionsMixin


class UserManager(BaseUserManager):
    use_in_migrations = True
    '''
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    '''
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=UserManager.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user    
    

    def create_superuser(self, email, password, **extra_fields):
        '''
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)
        '''    
        u = self.create_user(email=email,password=password)
        u.is_admin = True
        u.save(using=self._db)
        return u
    


class UserModel(AbstractUser , PermissionsMixin):
    ''' User 모델 확장 '''
    email = models.EmailField(unique = True, verbose_name='이메일' , max_length=255)
    username = models.CharField(max_length=20, verbose_name='이름')
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='가입일')
    is_active = models.BooleanField(default=True, verbose_name='활성화 여부')
    is_admin = models.BooleanField(default=False, verbose_name='관리자 여부')
    is_superuser = models.BooleanField(default=False, verbose_name='슈퍼 관리자. 관리자 여부')
    
    photo = models.FileField(blank=True , upload_to='zsy_user_info/%y%m%d/')
      
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()    

    class Meta:
        db_table = 'zsy_user_info' # 테이블 이름 지정
    
    def get_full_name(self):
        return self.email
    
    def get_shot_name(self):
        return self.email
    
    def __str__(self):
        return self.email
    

    




'''
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
   ''' 