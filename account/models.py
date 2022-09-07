from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from .managers import CustomerUserManager

# Create your models here.

class User(AbstractBaseUser,PermissionsMixin):
    name=models.CharField(max_length=50,null=True,blank=True)
    email=models.EmailField(max_length=50,unique=True,blank=False,null=False)
    mobile=models.CharField(max_length=15,blank=True,null=True)
    otp = models.CharField(max_length=6)
    is_phone_verified = models.BooleanField(default=False)
    status = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomerUserManager()
    
    class Meta:
        verbose_name_plural = "CustomUser"
        managed = True


class Book(models.Model):
    book_name = models.CharField(max_length=100)
    book_title = models.CharField(max_length=100)
    book_author = models.CharField(max_length=100)
    publish_date= models.DateTimeField(auto_now=True)
    update_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.book_name


    
