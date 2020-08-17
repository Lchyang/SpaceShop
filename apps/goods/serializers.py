from rest_framework import serializers
from .models import Goods
from .models import GoodCategories


class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = '__all__'


class GoodCategoriesSerializer3(serializers.ModelSerializer):
    goods = GoodsSerializer(many=True)

    class Meta:
        model = GoodCategories
        fields = '__all__'


class GoodCategoriesSerializer2(serializers.ModelSerializer):
    goods = GoodsSerializer(many=True)
    sub_cat = GoodCategoriesSerializer3(many=True)

    class Meta:
        model = GoodCategories
        fields = '__all__'


class GoodCategoriesSerializer(serializers.ModelSerializer):
    goods = GoodsSerializer(many=True)
    sub_cat = GoodCategoriesSerializer2(many=True)

    class Meta:
        model = GoodCategories
        fields = '__all__'
