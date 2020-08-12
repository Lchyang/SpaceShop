from rest_framework import serializers
from .models import Goods


class GoodsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True, help_text="商品id")
    class Meta:
        model = Goods
        fields = '__all__'
