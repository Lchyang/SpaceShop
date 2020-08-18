from datetime import datetime

from django.contrib.auth import get_user_model
from django.db import models

from goods.models import Goods

User = get_user_model()


class UserFav(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户名", related_name='user_favs')
    good = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name="商品")
    created_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    def __str__(self):
        return self.good.name

    class Meta:
        verbose_name = '商户收藏商品'
        verbose_name_plural = verbose_name
        # 收藏是基于用户的所以要构建联合唯一
        unique_together = ('user', 'good')


class UserLeaveMsg(models.Model):
    MSG_TYPE = (
        (1, '留言'),
        (2, '投诉'),
        (3, '询问'),
        (4, '售后'),
        (5, '求购')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户名", related_name='leave_msg')
    msg_type = models.IntegerField(default=1, choices=MSG_TYPE, verbose_name='留言类型')
    title = models.CharField(max_length=50, verbose_name='留言主题')
    content = models.TextField(verbose_name='留言内容')
    file = models.FileField(null=True, blank=True, upload_to='message/files', verbose_name='留言文件')
    created_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '用户留言'
        verbose_name_plural = verbose_name


class UserAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户名", related_name='address')
    province = models.CharField(max_length=20, verbose_name='省份')
    city = models.CharField(max_length=20, verbose_name='城市')
    district = models.CharField(max_length=20, verbose_name='地区')
    signer_name = models.CharField(max_length=20, verbose_name='收货人')
    address = models.CharField(max_length=100, verbose_name='详细地址')
    signer_mobile = models.CharField(max_length=11, verbose_name='收货人电话')
    created_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    def __str__(self):
        return "{},{}".format(self.user.name, self.signer_name)

    class Meta:
        verbose_name = '用户收货地址'
        verbose_name_plural = verbose_name
