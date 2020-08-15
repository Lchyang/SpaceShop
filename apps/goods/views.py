from django.http import Http404

from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import mixins

from .models import Goods, GoodCategories
from .serializers import GoodsSerializer, GoodCategoriesSerializer


# APIView事例
class GoodsListView(APIView):
    """
    get:
    Return a list of all the existing users.

    post:
    Create a new user instance.
    """

    def get(self, request):
        # 过滤
        price_min = request.query_params.get('price_min')
        price_max = request.query_params.get('price_max')
        goods = Goods.objects.all()
        if not price_min:
            price_min = 0
        if not price_max:
            price_max = 10000
        if price_max or price_min:
            goods = goods.filter(sales_price__gte=price_min, sales_price__lte=price_max)

        # 搜索
        name = request.query_params.get('name', '')
        if name:
            goods = goods.filter(name__contains=name)

        # 排序
        order_filed = request.query_params.get('order_filed', '')
        if order_filed:
            goods = goods.order_by(order_filed)

        # 获取商品列表自定义分页
        _paginator = PageNumberPagination()
        _paginator.page_size = 10
        page = _paginator.paginate_queryset(goods, request, view=self)
        serializer = GoodsSerializer(page, many=True)
        return _paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = GoodsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GoodDetailView(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, pk):
        try:
            return Goods.objects.get(pk=pk)
        except Goods.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        goods = self.get_object(pk)
        serializer = GoodsSerializer(goods)
        return Response(serializer.data)

    def put(self, request, pk):
        good = self.get_object(pk)
        serializer = GoodsSerializer(good, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        good = self.get_object(pk)
        good.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# 分类用viewset写
class CategoriesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = GoodCategories.objects.all()
    serializer_class = GoodCategoriesSerializer


# 测试当数据不是从数据库里面取出的情况下如何使用rest framework
from utils.db_tools.data.data import row_data


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 1000


class NoDatabaseDataListViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    # queryset 可以任意传一个，不传的话会报错，但是对逻辑结果没有作用
    queryset = GoodCategories.objects.all()
    # serializer_class 在生成文档时有用
    serializer_class = GoodsSerializer

    # 分页作用，因为内部逻辑分页传入的是list对象，但是filter传入的queryset,所以分页可以使用rest framework
    # 但是过滤和搜索要自己实现
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return

    def list(self, request, *args, **kwargs):
        queryset = row_data
        page = self.paginate_queryset(queryset)
        if page is not None:
            return self.get_paginated_response(page)
        return Response(row_data)

    def create(self, request, *args, **kwargs):
        data = request.data
        headers = self.get_success_headers(data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)
