from rest_framework import serializers

from .models import UserFav


class UserFavSerializer(serializers.ModelSerializer):
    # 自动获取当前用户名，因为收藏操作应该默认是当前用户
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = UserFav
        fields = ('user', 'good', 'id')
