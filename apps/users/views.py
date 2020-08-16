import random

from django.db.models import Q
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

from rest_framework import viewsets, status
from rest_framework import mixins
from rest_framework.response import Response

from .models import VerifyCode
from .serializers import VerifyMobileSerializer
from .send_sms import YunPianSms
from SpaceShop.settings import YUNPIAN_APIKEY, YUNPIAN_TEXT

User = get_user_model()


class CustomBackend(ModelBackend):
    """自定义用户认证"""

    # 如果要自定义用户认证的话，要继承ModelBackend 然后重载authenticate这个方法
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # 当用户名传入的事username或者mobile都应该认证成功
            user = User.objects.get(Q(username=username) | Q(mobile=username))
            if user.check_password(password):
                return user
        except NotImplementedError or Exception:
            return None


class VerifyMobileViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = VerifyCode.objects.all()
    serializer_class = VerifyMobileSerializer

    # 生成验证码
    @staticmethod
    def generator_code():
        seeds = '0123456789'
        code = ''
        for i in range(4):
            code += random.choice(seeds)
        return code

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        mobile = serializer.validated_data.get('mobile', None)
        code = self.generator_code()
        text = YUNPIAN_TEXT.format(code)
        # TODO 发送短信 应该使用celery
        yun_pian = YunPianSms(YUNPIAN_APIKEY)
        res = yun_pian.send_sms(mobile=mobile, text=text)
        if res.get('code', None) == 0:
            verify_instance = VerifyCode(code=code, mobile=mobile)
            verify_instance.save()
            return Response({'mobile': mobile, 'msg': res['msg']}, status=status.HTTP_201_CREATED)
        else:
            return Response({'mobile': mobile, 'msg': res['msg']}, status=status.HTTP_400_BAD_REQUEST)
