import re
import datetime

from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import VerifyCode

User = get_user_model()


class VerifyMobileSerializer(serializers.Serializer):
    # TODO 发送短信验证手机号码逻辑
    mobile = serializers.CharField(max_length=11)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    @staticmethod
    def validate_mobile(value):
        """
        验证手机号码格式
        """

        if not re.match(r"^1[35678]\d{9}$", value):
            raise serializers.ValidationError("手机号码格式不正确")

        if User.objects.filter(mobile=value).count():
            raise serializers.ValidationError("用户已经存在")

        one_minute_ago = datetime.datetime.now() - datetime.timedelta(hours=0, minutes=1, seconds=0)
        if VerifyCode.objects.filter(modified_time__gt=one_minute_ago, mobile=value).count():
            raise serializers.ValidationError("距离上次发送时间未超过一分钟")

        return value


class RegisterSerializer(serializers.ModelSerializer):
    # TODO 注册逻辑
    # write_only 只有反向序列化的时候验证此字段， read_only 当正向序列化的时候验证此字段
    code = serializers.CharField(allow_null=True, allow_blank=True, max_length=4,
                                 min_length=4, label='验证码', write_only=True)
    # UniqueValidator 对数据库里面unique=True的字段进行验证，message返回验证错误时的信息
    username = serializers.CharField(max_length=11, min_length=11, label='用户名',
                                     validators=[UniqueValidator(queryset=User.objects.all(),
                                                                 message='用户已经存在')])
    # style 密码输入为密文
    password = serializers.CharField(style={'input_type': 'password'}, label='密码', write_only=True)

    '''
    # 该功能可以用django signal 完成, 以被替代，留在这做参考
    def create(self, validated_data):
        # 因为是注册，必须先创建用户，返回用户实例,然后把密码保存成密文
        instance = super().create(validated_data)
        instance.set_password(validated_data['password'])
        instance.save()
        return instance
    '''

    def validate_code(self, code):
        """
        field 级别验证 code值为该字段值，可以是其他名字
        """
        # initial_data 是验证之前的参数， validate_data是验证时候的参数
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
        # code 字段只需要验证功能，当验证结束后需要删除否则存入数据库的时候会抛出异常
        del attrs['code']
        attrs['mobile'] = attrs['username']
        return attrs

    class Meta:
        model = User
        fields = ['username', 'code', 'password']
