import re
import datetime

from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import VerifyCode

User = get_user_model()


class VerifyMobileSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=11)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    @staticmethod
    def validate_mobile(value):
        if not re.match(r"^1[35678]\d{9}$", value):
            raise serializers.ValidationError("手机号码格式不正确")

        if User.objects.filter(mobile=value).count():
            raise serializers.ValidationError("用户已经存在")

        one_minute_ago = datetime.datetime.now() - datetime.timedelta(hours=0, minutes=1, seconds=0)
        if VerifyCode.objects.filter(modified_time__gt=one_minute_ago, mobile=value).count():
            raise serializers.ValidationError("距离上次发送时间未超过一分钟")

        return value
