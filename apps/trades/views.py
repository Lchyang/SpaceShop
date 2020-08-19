from rest_framework import viewsets, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from apps.utils.custom_permission import IsOwnerOrReadOnly
from .models import ShoppingCart
from .serializers import ShoppingCartSerializer
from .serializers import ShoppingCartListSerializer


class ShoppingCartViewSet(viewsets.ModelViewSet):
    """
    购物车逻辑：
    如果存在商品nums+1 如果不存在则创建
    商品添加减少用update
    """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    lookup_field = 'goods_id'

    def get_queryset(self):
        return ShoppingCart.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return ShoppingCartListSerializer
        else:
            return ShoppingCartSerializer

