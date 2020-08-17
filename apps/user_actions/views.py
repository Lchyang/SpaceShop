from rest_framework import viewsets, permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import UserFav
from .serializers import UserFavSerializer

# TODO 看是否需要重构，解耦
class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.user == request.user


class UserFavViewSet(viewsets.ModelViewSet):
    """
    用户收藏
    """
    serializer_class = UserFavSerializer
    # 权限验证IsAuthenticated只验证是否登录，当执行删除操作的时候要验证删除的数据user是否是当前的user
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    # session方式是因为drf文档的登录方式为session
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    # 用户收藏是在商品详情页面，当用户收藏的时候传入的是商品的id，所以查找用户收藏的表的时候用good_id,而不是pk
    lookup_field = 'good_id'

    def get_queryset(self):
        """过滤当前用户的数据"""
        return UserFav.objects.filter(user=self.request.user)
