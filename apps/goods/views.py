from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as django_filters

from rest_framework import viewsets
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination

from .models import Goods, GoodCategories
from .serializers import GoodsSerializer, GoodCategoriesSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 1000


class GoodsFilter(django_filters.FilterSet):
    pricemin = django_filters.NumberFilter(field_name="sales_price", lookup_expr='gte')
    pricemax = django_filters.NumberFilter(field_name="sales_price", lookup_expr='lte')
    top_category = django_filters.NumberFilter(field_name='category', method='get_top_category')

    def get_top_category(self, queryset, name, value):
        return queryset.filter(Q(category_id=value) | Q(category__parent_category_id=value) | Q(
            category__parent_category__parent_category_id=value))

    class Meta:
        model = Goods
        fields = ['pricemin', 'pricemax', 'top_category']


class GoodsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filter_class = GoodsFilter
    search_fields = ['name']
    ordering_fields = ['sales_price', 'sold_nums']


class CategoriesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = GoodCategories.objects.filter(category_type=1)
    serializer_class = GoodCategoriesSerializer
