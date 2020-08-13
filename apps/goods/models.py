from datetime import datetime
from django.db import models
from DjangoUeditor.models import UEditorField


class GoodCategories(models.Model):
    """商品类别"""
    CATEGORY_CHOICE = (
        (1, '一级类目'),
        (2, '二级类目'),
        (3, '三级类目'),
    )
    name = models.CharField(default='', max_length=60, verbose_name="商品类别名称")
    code = models.CharField(default='', max_length=30, verbose_name='商品类别编号')
    desc = models.TextField(default='', verbose_name="类别描述", help_text="类别描述")
    # 存在三级类别，当此字段为空的时候为父类别，有字段的时候为子类别，related_name 父类查询子类时使用
    parent_category = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE, related_name='sub_cat',
                                        verbose_name="父类别")
    category_type = models.IntegerField(choices=CATEGORY_CHOICE, verbose_name="商品类目级别")
    created_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    modified_time = models.DateTimeField(verbose_name='修改时间')

    def save(self, *args, **kwargs):
        self.modified_time = datetime.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "商品分类"
        verbose_name_plural = verbose_name


class Goods(models.Model):
    """商品"""
    category = models.ForeignKey(GoodCategories, default='', on_delete=models.CASCADE, related_name='goods',
                                 verbose_name="商品类别")
    name = models.CharField(max_length=60, verbose_name="商品名称")
    goods_sn = models.CharField(max_length=50, verbose_name="商品唯一货号")
    market_price = models.FloatField(default=0, verbose_name="商品市场价格")
    sales_price = models.FloatField(default=0, verbose_name="商品促销价格")
    desc = models.TextField(null=True, blank=True, verbose_name="商品描述")
    goods_front_image = models.ImageField(upload_to="goods/images/cover", null=True, blank=True, verbose_name="封面图")
    ship_free = models.BooleanField(default=True, verbose_name="是否承担运费")
    # django富文本编辑
    goods_desc = UEditorField(verbose_name=u"内容", imagePath="goods/images/", width=1000, height=300,
                              filePath="goods/files/", default='')
    sold_nums = models.IntegerField(default=0, verbose_name="商品销量")
    stored_nums = models.IntegerField(default=0, verbose_name="商品库存数量")
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


class GoodImages(models.Model):
    """商品轮播图"""
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, related_name='images', verbose_name='商品')
    images = models.ImageField(upload_to='goods/images/carousel', verbose_name='商品图片')
    created_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    modified_time = models.DateTimeField(verbose_name='修改时间')

    def save(self, *args, **kwargs):
        self.modified_time = datetime.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.goods.name

    class Meta:
        verbose_name = "商品图片"
        verbose_name_plural = verbose_name
