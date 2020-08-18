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
