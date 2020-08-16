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


class RegisterSerializer(serializers.ModelSerializer):
    # TODO 用户存在是异常处理，code表单可以为空
    code = serializers.CharField(max_length=4, min_length=4, label='验证码', write_only=True)
    username = serializers.CharField(max_length=11, min_length=11, label='用户名')
    password = serializers.CharField(style={'input_type': 'password'}, label='密码', write_only=True)

    def create(self, validated_data):
        instance = super().create(validated_data)
        instance.set_password(validated_data['password'])
        instance.save()
        return instance

    def validate_code(self, code):
        username = self.initial_data.get('username', None)
        verify_code = VerifyCode.objects.filter(mobile=username).order_by("-created_time")
        if verify_code:
            last_code = verify_code[0]
            five_minute_ago = datetime.datetime.now() - datetime.timedelta(hours=0, minutes=5, seconds=0)
            if last_code.modified_time < five_minute_ago:
                raise serializers.ValidationError("验证码超时")

            if last_code.code != code:
                raise serializers.ValidationError("验证码错误")
        else:
            raise serializers.ValidationError("该用户没有获取到验证码")

    def validate(self, attrs):
        del attrs['code']
        attrs['mobile'] = attrs['username']
        return attrs

    class Meta:
        model = User
        fields = ['username', 'code', 'password']
