from rest_framework import viewsets
from rest_framework import mixins
from .models import Goods
from .serializers import GoodsSerializer


class GoodsView(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
