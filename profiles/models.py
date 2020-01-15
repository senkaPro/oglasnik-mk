from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager as Manager
from django.db import models
from PIL import Image


class UserManager(Manager):
    use_in_migrations =True

    def _create_user(self,email,password,**kwargs):

        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        username = email.split('@',1)[0]
        user = self.model(username=username,email=email,**kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self,email=None,password=None,**kwargs):
        kwargs.setdefault('is_staff',False)
        kwargs.setdefault('is_superuser',False)

        return self._create_user(email,password,**kwargs)

    def create_superuser(self,email,password,**kwargs):
        kwargs.setdefault('is_staff',True)
        kwargs.setdefault('is_superuser',True)

        if kwargs.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if kwargs.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email,password,**kwargs)




class User(AbstractUser):

    username = models.CharField(max_length=30,unique=True)
    email = models.EmailField('Email Address',unique=True,blank=False,null=False)

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()



class Profile(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE,editable=False)
    screen_name = models.CharField(max_length=30,blank=True,null=True)
    location = models.CharField(max_length=30,blank=True,null=True)
    adds_added = models.IntegerField(default=0)
    profile_pic = models.ImageField(upload_to=settings.MEDIA_URL)


    def __str__(self):
        return self.user.username
