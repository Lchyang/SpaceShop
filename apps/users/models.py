from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class UserProfile(AbstractUser):
    GENDER_CHOICE = (
        (1, '女'),
        (2, '男')
    )
    name = models.CharField(max_length=30, blank=True, null=True, verbose_name='用户名')
    gender = models.IntegerField(choices=GENDER_CHOICE, default=1, verbose_name="性别")
    birthday = models.DateTimeField(null=True, blank=True, verbose_name='出生日期')
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name="手机号")
    created_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    modified_time = models.DateTimeField(verbose_name='修改时间')

    def save(self, *args, **kwargs):
        self.modified_time = datetime.now()
        super().save(*args, **kwargs)

    def __str__(self):
        if self.name:
            return self.name
        return self.username

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name
