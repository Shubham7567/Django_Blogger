from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager


class MyAccountManager(BaseUserManager):
    def create_user(self,username,email,password=None):
        if not username:
            raise ValueError("User must have a username")
        if not email:
            raise ValueError("User must have an email")

        user = self.model(
            email = self.normalize_email(email),
            username = username
        )
        user.set_password(password)

        user.save(using=self._db)
        return user

    def create_superuser(self,username,email,password):
        user = self.create_user(
            email = self.normalize_email(email),
            password = password,
            username = username
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user

GENDER_CHOICES = (("select Gender","Select Gender"),("male","Male"),("female","Female"),("others","Others"))

class Account(AbstractBaseUser):
    username = models.CharField(verbose_name="Username",max_length=100,unique=True)
    email = models.EmailField(verbose_name="Email",max_length=100,unique=True)
    name = models.CharField(verbose_name="Name",max_length=100,blank=True,null=True)
    profile_pic = models.ImageField(verbose_name="Profile Picture",default="avatar.png",upload_to="myprofile/%d%m%y")
    gender = models.CharField(verbose_name="Gender",choices=GENDER_CHOICES,default="male",max_length=20,null=True,blank=True)
    date_joined = models.DateTimeField(verbose_name="Date Joined",auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="Last Login",auto_now=True)
    is_admin = models.BooleanField(verbose_name="Is Admin",default=False)
    is_active = models.BooleanField(verbose_name="Is Active",default=True)
    is_staff = models.BooleanField(verbose_name="Is Staff User",default=False)
    is_superuser = models.BooleanField(verbose_name="Is Super User",default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyAccountManager()
    

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
