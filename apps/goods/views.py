from rest_framework import viewsets
from rest_framework import mixins
from .models import Goods
from .serializers import GoodsSerializer


class GoodsView(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    """
    list:
    商品列表
    retrieve:
    获取商品详情
    id: 商品的id
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
