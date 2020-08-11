import os
import sys

pwd = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(pwd)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SpaceShop.settings')

import django

django.setup()

from apps.goods.models import Goods, GoodsImages, GoodsCategorys

from utils.db_tools.data.product_data import row_data

for good in row_data:
    good_instance = Goods()
    good_instance.name = good['name']
    good_instance.desc = good['desc'] if good['desc'] else ''
    good_instance.sales_price = good['sale_price'].replace('￥', '').replace('元', '')
    good_instance.market_price = good['market_price'].replace('￥', '').replace('元', '')
    good_instance.goods_desc = good['goods_desc'] if good['goods_desc'] is not None else ''
    good_instance.goods_front_image = good['images'][0] if good['images'] else ''

    category_name = good['categorys'][-1]
    category = GoodsCategorys.objects.filter(name=category_name)
    if category:
        good_instance.category = category[0]
    good_instance.save()

    for image in good['images']:
        image_instance = GoodsImages()
        image_instance.images = image
        image_instance.goods = good_instance
        image_instance.save()
