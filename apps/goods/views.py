from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as django_filters

from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination

from .models import GoodCategories
from .models import Goods
from .serializers import GoodCategoriesSerializer
from .serializers import GoodsSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    page_size_query_description = '每页数量'
    page_query_param = "page"
    page_query_description = '页数'
    max_page_size = 1000


class GoodsFilter(django_filters.FilterSet):
    """
    基于django-filter的过滤函数
    """
    pricemin = django_filters.NumberFilter(field_name="sales_price", lookup_expr='gte')
    pricemax = django_filters.NumberFilter(field_name="sales_price", lookup_expr='lte')
    # method 方式，获取字段
    top_category = django_filters.NumberFilter(field_name='category', method='get_top_category')

    @staticmethod
    def get_top_category(queryset, _, value):
        """
        联合查询方式，过滤出一个子类下面的所有商品
        """
        return queryset.filter(Q(category_id=value) | Q(category__parent_category_id=value) | Q(
            category__parent_category__parent_category_id=value))

    class Meta:
        model = Goods
        fields = ['pricemin', 'pricemax', 'top_category', 'is_hot']


class GoodsSearch(SearchFilter):
    search_description = '输入搜索内容'


class GoodsOrding(OrderingFilter):
    ordering_description = '排序内容'


class GoodsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    商品列表和详情
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, GoodsSearch, GoodsOrding]
    filter_class = GoodsFilter
    search_fields = ['name']
    ordering_fields = ['sales_price', 'sold_nums']


class CategoriesViewSet(viewsets.ReadOnlyModelViewSet):
    """
    商品分类列表和详情
    """
    queryset = GoodCategories.objects.filter(category_type=1)
    serializer_class = GoodCategoriesSerializer
