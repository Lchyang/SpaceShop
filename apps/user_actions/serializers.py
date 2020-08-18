from rest_framework import serializers

from .models import UserFav
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
