import os
import sys

pwd = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(pwd)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SpaceShop.settings')

import django

django.setup()

from apps.goods.models import Goods, GoodsImages, GoodsCategorys

from utils.db_tools.data.category_data import row_data

for category in row_data:
    category_instance = GoodsCategorys()
    category_instance.name = category['name']
    category_instance.code = category['code']
    category_instance.category_type = 1
    category_instance.save()
    for sub_cate in category['sub_categorys']:
        sub_category_instance = GoodsCategorys()
        sub_category_instance.name = sub_cate['name']
        sub_category_instance.code = sub_cate['code']
        sub_category_instance.parent_category = category_instance
        sub_category_instance.category_type = 2
        sub_category_instance.save()
        for sub_sub_cate in sub_cate['sub_categorys']:
            su_category_instance = GoodsCategorys()
            su_category_instance.name = sub_sub_cate['name']
            su_category_instance.code = sub_sub_cate['code']
            su_category_instance.parent_category = sub_category_instance
            su_category_instance.category_type = 3
            su_category_instance.save()

