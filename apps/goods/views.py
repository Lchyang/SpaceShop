from django.http import Http404

from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

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
        """获取商品列表自定义分页"""
        goods = Goods.objects.all()
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


# genericsAPIView示例
class CategoriesListCreateView(generics.ListCreateAPIView):
    queryset = GoodCategories.objects.all()
    serializer_class = GoodCategoriesSerializer


class CategoriesRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GoodCategories.objects.all()
    serializer_class = GoodCategoriesSerializer
