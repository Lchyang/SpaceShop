from rest_framework import serializers
from goods.models import Goods


class ShoppingCartSerializer(serializers.Serializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault)
    goods = serializers.PrimaryKeyRelatedField(queryset=Goods.objects.all())
    nums = serializers.IntegerField(required=True, min_value=1, error_messages={
        "required": "请选择商品购买数量",
        "min_value": "商品数量不能小于1"
    })

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
