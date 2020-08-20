import random

from django.db.models import Q
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.conf import settings

from rest_framework import viewsets
from rest_framework import status
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework_jwt.utils import jwt_payload_handler
from rest_framework_jwt.utils import jwt_encode_handler
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import RegisterSerializer
from .serializers import UserCenterSerializer
from .serializers import VerifyMobileSerializer

from .models import VerifyCode
from .send_sms import YunPianSms

User = get_user_model()


class CustomBackend(ModelBackend):
    """
    自定义用户认证
    如果要自定义用户认证的话，要继承ModelBackend 然后重载authenticate这个方法
    """

    # 希望当用户传入手机号，和username时都能验证通过，django默认的是使用username和email所以需要重载
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # 当用户名传入的事username或者mobile都应该认证成功
            user = User.objects.get(Q(username=username) | Q(mobile=username))
            if user.check_password(password):
                return user
        except NotImplementedError or Exception:
            return None


class VerifyMobileViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    """
    注册之前要先发送验证码，到手机号，发送成功之后将验证码，手机号存入数据库
    """
    # TODO 验证码逻辑
    queryset = VerifyCode.objects.all()
    serializer_class = VerifyMobileSerializer

    @staticmethod
    def generator_code():
        seeds = '0123456789'
        code = ''
        for i in range(4):
            # 尽量不要再循环中使用+=拼接字符串，比较好的方式时创建列表然后join
            code += random.choice(seeds)
        return code

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        mobile = serializer.validated_data.get('mobile', None)
        code = self.generator_code()
        # 拼接发送的短信
        text = settings.YUNPIAN_TEXT.format(code)
        yun_pian = YunPianSms(settings.YUNPIAN_APIKEY)
        # TODO 发送短信 应该使用celery
        res = yun_pian.send_sms(mobile=mobile, text=text)
        if res.get('code', None) == 0:
            verify_instance = VerifyCode(code=code, mobile=mobile)
            verify_instance.save()
            return Response({'mobile': mobile, 'msg': res['msg']}, status=status.HTTP_201_CREATED)
        else:
            return Response({'mobile': mobile, 'msg': res['msg']}, status=status.HTTP_400_BAD_REQUEST)


class RegisterViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    """
    注册用户，主要逻辑就是获取手机验证码后，验证当前手机号的验证码,合法后把user存入数据库, 主要逻辑在serializer

    关于initial_data  validated_data data 的区别
    反序列化：
    initial_data 在调用.is_valid()之前
    validated_data 在调用.is_valid()之后
    validated_data 是验证成功之后的数据 失败则没有数据
    序列化：
    直接调用 data
    """
    # TODO 注册逻辑回头仔细看一下
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        """
        因为注册的逻辑是注册之后就登录，所以需要把username token返回给前端
        token 的生成逻辑可以参考rest_framework_jwt 源码
        """

        '''
        如果把个人信息修改集成到这个类，可以使用动态的方式分配行为
        def get_serializer_class(self):
            if self.action == 'retrieve':
                return UserDetailSerializer
            elif self.action == 'create':
                return UserRegSerializer
            return UserDetailSerializer

        def get_permissions(self):
            if self.action == 'retrieve':
                return [permissions.IsAuthenticated()]
            elif self.action == 'create':
                return []
            return []
        '''

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        data = serializer.data
        data['token'] = jwt_encode_handler(jwt_payload_handler(user))
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()


class UserCenterViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.UpdateModelMixin):
    """
    用户个人中心获取数据
    """
    serializer_class = UserCenterSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (SessionAuthentication, JSONWebTokenAuthentication)

    def get_queryset(self):
        return User.objects.filter(username=self.request.user.username)

    def get_object(self):
        """更新用户信息的时候传入id，但是id不起作用只是用于url格式"""
        return self.request.user
