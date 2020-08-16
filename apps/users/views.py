from django.db.models import Q
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

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
