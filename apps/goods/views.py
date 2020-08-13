from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from .models import Goods, GoodCategories
from .serializers import GoodsSerializer, GoodCategoriesSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000


class GoodsView(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    """
    list:
    商品列表
    retrieve:
    获取商品详情
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = StandardResultsSetPagination


class GoodCategoriesView(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    """
    list:
    获取商品类别列表
    retrieve:
    获取商品分类详情
    """
    queryset = GoodCategories.objects.filter(category_type=1)
    serializer_class = GoodCategoriesSerializer
