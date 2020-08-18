from rest_framework import serializers

from .models import UserFav
from .models import UserLeaveMsg
from .models import UserAddress
from goods.models import Goods


class UserFavSerializer(serializers.ModelSerializer):
    # 自动获取当前用户名，因为收藏操作应该默认是当前用户
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = UserFav
        fields = ('user', 'good', 'id')


class FavGoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = ('sales_price', 'name', 'id')


class UserFavListSerializer(serializers.ModelSerializer):
    good = FavGoodSerializer()

    class Meta:
        model = UserFav
        fields = ('good', 'id')


class UserLeaveMsgSerializer(serializers.ModelSerializer):
    # Todo 添加一些表单验证字段
    created_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = UserLeaveMsg
        fields = '__all__'


class UserAddressSerializer(serializers.ModelSerializer):
    # todo 手机号码验证
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = UserAddress
        exclude = ('created_time',)
