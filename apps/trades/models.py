from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model

from goods.models import Goods

User = get_user_model()


class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
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


class Order(models.Model):
    PAYING_STATUS = (
        ("TRADE_SUCCESS", "成功"),
        ("TRADE_CLOSED", "超时关闭"),
        ("WAIT_BUYER_PAY", "交易创建"),
        ("TRADE_FINISHED", "交易结束"),
        ("paying", "待支付"),
    )
    # todo 一个订单要包含哪些基本的字段
    # 用于支付宝交易是返回数据
    order_sn = models.CharField(max_length=30, null=True, blank=True, verbose_name="订单编号")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    paying_status = models.CharField(max_length=30, default="paying", verbose_name="订单支付状态")
    trade_no = models.CharField(max_length=100, unique=True, null=True, blank=True, verbose_name="交易号")
    created_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    post_script = models.CharField(max_length=200,null=True, blank=True, verbose_name="订单留言")
    order_mount = models.FloatField(default=0.0, verbose_name="订单金额")
    pay_time = models.DateTimeField(null=True, blank=True, verbose_name="支付时间")
    # 用户信息
    address = models.CharField(max_length=100, default="", verbose_name="收货地址")
    signer_name = models.CharField(max_length=20, default="", verbose_name="签收人")
    singer_mobile = models.CharField(max_length=11, verbose_name="联系电话")

    def __str__(self):
        return "{},{}".format(self.order_sn, self.user.name)

    class Meta:
        verbose_name = "订单"
        verbose_name_plural = verbose_name


class OrderGoods(models.Model):
    nums = models.IntegerField(verbose_name="订单商品数量")
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name="商品")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="订单", related_name="order_goods")
    created_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    def __str__(self):
        return self.goods.name

    class Meta:
        verbose_name = "订单"
        verbose_name_plural = verbose_name
