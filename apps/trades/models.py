from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model

from goods.models import Goods

User = get_user_model()


class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="用户")
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name="商品")
    nums = models.IntegerField(verbose_name="商品数量")
    created_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    modified_time = models.DateTimeField(verbose_name='修改时间')

    def save(self, *args, **kwargs):
        self.modified_time = datetime.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return "{},{}".format(self.user.name, self.goods.name)

    class Meta:
        verbose_name = "购物车"
        verbose_name_plural = verbose_name
