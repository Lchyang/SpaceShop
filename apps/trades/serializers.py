from rest_framework import serializers
from goods.models import Goods
from .models import ShoppingCart
from goods.serializers import GoodsSerializer


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
