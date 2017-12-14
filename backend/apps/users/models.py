from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser



class UserProfile(AbstractUser):
    """
    用户
    """
    # id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=30, null=False, blank=True, verbose_name="姓名")
    jobnumber = models.CharField(max_length=30, null=False, blank=True, verbose_name="工号")
    birthday = models.DateField(null=True, blank=True, verbose_name="出生年月")
    entrydate = models.DateField(null=True, blank=True, verbose_name="入职日期")
    gender = models.CharField(max_length=6, choices=(("male", "男"), ("female", "女")), default="female", verbose_name="性别")
    mobile = models.CharField(null=True, blank=True, max_length=11, verbose_name="电话")
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name="邮箱")

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username