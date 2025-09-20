from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.utils.translation import gettext as _

# Create your models here.
class UserManager(BaseUserManager):
   def create_user(self,user_name,email,password,**extra_fields):
      if not user_name:
         raise ValueError(_("username must be set"))
      if not email:
         raise ValueError(_("email must be set"))
      email=self.normalize_email(email)
      user=self.model(user_name=user_name,email=email,**extra_fields)
      user.set_password(password)
      user.save()
      return user
   def create_superuser(self,user_name,email,password,**extra_fields):
      extra_fields.setdefault('is_staff',True)
      extra_fields.setdefault('is_superuser',True)
      extra_fields.setdefault('is_active',True)
      extra_fields.setdefault('is_verified',True)

      if extra_fields.get('is_staff') is not True:
         raise ValueError(_("superuser must have is_staff"))
      if extra_fields.get('is_superuser') is not True:
         raise ValueError(_("superuser must have is_superuser"))
      if extra_fields.get('is_active') is not True:
         raise ValueError(_("superuser must have is_active"))
      return self.create_user(user_name,email,password,**extra_fields)


class User(AbstractBaseUser,PermissionsMixin):
   user_name=models.CharField(max_length=255,unique=True)
   email=models.EmailField(max_length=255,unique=True)
   is_staff=models.BooleanField(default=False)
   is_active=models.BooleanField(default=True)
   is_superuser=models.BooleanField(default=False)
   is_verified=models.BooleanField(default=False)
   created_date=models.DateTimeField(auto_now_add=True)
   updated_date=models.DateTimeField(auto_now=True)
   image_profile=models.ImageField(upload_to='account/profile',null=True,blank=True)

   USERNAME_FIELD='user_name'
   REQUIRED_FIELDS=['email']

   objects=UserManager()
   def __str__(self):
      return self.email