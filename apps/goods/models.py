from datetime import datetime
from django.db import models


class GoodsModel(models.Model):
    """商品"""
    name = models.CharField(max_length=60, default='', verbose_name="商品名称")
    market_price = models.IntegerField(max_length=20, default=0, verbose_name="商品市场价格")
    sales_price = models.IntegerField(max_length=20, default=0, verbose_name="商品促销价格")
    desc = models.CharField(max_length=120, null=True, blank=True, verbose_name="商品描述")
    image = models.ImageField(upload_to='', verbose_name="商品图片")
    nums = models.IntegerField(max_length=10, default='0', verbose_name="商品销量")
    created_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    modified_time = models.DateTimeField(verbose_name='修改时间')

    def save(self, *args, **kwargs):
        """每次修改时保存修改时间"""
        self.modified_time = datetime.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "商品"
        verbose_name_plural = verbose_name
