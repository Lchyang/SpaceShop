from rest_framework import viewsets
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import UserFav
from .models import UserLeaveMsg
from .models import UserAddress

from .serializers import UserFavSerializer
from .serializers import UserFavListSerializer
from .serializers import UserLeaveMsgSerializer
from .serializers import UserAddressSerializer

from apps.utils.custom_permission import IsOwnerOrReadOnly


class UserFavViewSet(viewsets.ModelViewSet):
    """
    list:
    用户收藏列表 因为列表要展示商品信息所以新建一个serializer比较合适
    """
    serializer_class = UserFavSerializer
    # 权限验证IsAuthenticated只验证是否登录，当执行删除操作的时候要验证删除的数据user是否是当前的user
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    # session方式是因为drf文档的登录方式为session
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    # 用户收藏是在商品详情页面，当用户收藏的时候传入的是商品的id，所以查找用户收藏的表的时候用good_id,而不是pk
    lookup_field = 'good_id'

    def get_serializer_class(self):
        if self.action == 'list':
            return UserFavListSerializer
        if self.action == 'retrieve':
            return UserFavSerializer
        return UserFavSerializer

    def get_queryset(self):
        """过滤当前用户的数据"""
        return UserFav.objects.filter(user=self.request.user)


class UserLeaveMsgViewSet(viewsets.ModelViewSet):
    """
    list:
    retrieve:
    update:
    create:
    """
    serializer_class = UserLeaveMsgSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def get_queryset(self):
        return UserLeaveMsg.objects.filter(user=self.request.user)


class UserAddressViewSet(viewsets.ModelViewSet):
    """
    收货地址
    """
    serializer_class = UserAddressSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def get_queryset(self):
        return UserAddress.objects.filter(user=self.request.user)
