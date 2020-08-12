from rest_framework import generics
from .models import Goods
from .serializers import GoodsSerializer


class GoodsView(generics.ListAPIView):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
