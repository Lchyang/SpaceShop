import time

from rest_framework import serializers
from django.conf import settings

from goods.models import Goods
from goods.serializers import GoodsSerializer
from apps.utils.alipay import AliPay
from .models import ShoppingCart, Order, OrderGoods
from random import Random


class ShoppingCartSerializer(serializers.Serializer):
    """
    购物车逻辑：
    如果存在商品nums+1 如果不存在则创建
    商品添加减少用update
    """

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    goods = serializers.PrimaryKeyRelatedField(queryset=Goods.objects.all())
    nums = serializers.IntegerField(required=True, min_value=1, error_messages={
        "required": "请选择商品购买数量",
        "min_value": "商品数量不能小于1"
    })

    def create(self, validated_data):
        goods = validated_data.get('goods', None)
        users = validated_data.get('user', None)
        nums = validated_data.get('nums', None)
        shop_cart = ShoppingCart.objects.filter(user=users, goods=goods)
        if shop_cart:
            shop_cart = shop_cart[0]
            shop_cart.nums += nums
            shop_cart.save()
        else:
            shop_cart = ShoppingCart.objects.create(**validated_data)
        return shop_cart

    def update(self, instance, validated_data):
        instance.nums = validated_data.get('nums', instance.nums)
        instance.save()
        return instance


class ShoppingCartListSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    nums = serializers.IntegerField(required=True, min_value=1, error_messages={
        "required": "请选择商品购买数量",
        "min_value": "商品数量不能小于1"
    })
    goods = GoodsSerializer()

    class Meta:
        model = ShoppingCart
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    order_sn = serializers.CharField(read_only=True)
    paying_status = serializers.CharField(read_only=True)
    trade_no = serializers.CharField(read_only=True)
    pay_time = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%S")
    created_time = serializers.DateTimeField(read_only=True)
    ali_pay_url = serializers.SerializerMethodField(read_only=True)

    # SerializerMethodField 通过函数构建字段，和下面generate_order_sn的区别，当使用obj时用SerializerMethodField.
    @staticmethod
    def get_ali_pay_url(obj):
        alipay = AliPay(
            appid=settings.APP_ID,
            app_notify_url=settings.NOTIFY_URL,
            app_private_key_path=settings.APP_PRIVATE_KEY_PATH,
            alipay_public_key_path=settings.ALIPAY_PUBLIC_KEY_PATH,
            # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
            debug=True,  # 默认False,
            return_url=settings.RETURN_URL
        )

        url = alipay.direct_pay(
            subject=obj.order_sn,
            out_trade_no=obj.order_sn,
            total_amount=obj.order_mount,
        )
        re_url = "https://openapi.alipaydev.com/gateway.do?{data}".format(data=url)
        return re_url

    def generate_order_sn(self):
        # 当前时间 + user.id + 两位随机数
        local_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
        user_id = self.context['request'].user.id
        # 必须得这样实例化一下，不然每次更新操作的时候random会从新执行
        random = Random()
        random_int = random.randint(10, 99)
        order_sn = "{}{}{}".format(local_time, user_id, random_int)

        return order_sn

    def validate(self, attrs):
        attrs['order_sn'] = self.generate_order_sn()
        return attrs

    class Meta:
        model = Order
        fields = '__all__'


class OrderGoodsSerializer(serializers.ModelSerializer):
    goods = GoodsSerializer()

    class Meta:
        model = OrderGoods
        fields = '__all__'


class OrderDetailSerializer(serializers.ModelSerializer):
    order_goods = OrderGoodsSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'
