# import requests
# import json
#
# conent = requests.get("http://127.0.0.1:8000/goods/?format=json&page=3")
#
# pydata = json.loads(conent.text)
#
# print(pydata["results"])
# row_data = pydata["results"]
# print(type(row_data))

row_data = [
    {'id': 21, 'name': '52度兰陵·紫气东来1600mL山东名酒', 'goods_sn': '', 'market_price': 42.0, 'sales_price': 35.0,
     'desc': '', 'goods_front_image': '/media/goods/images/13_P_1448947460386.jpg', 'ship_free': True,
     'goods_desc': '<p><img src="/media/goods/images/2_20170719161405_249.jpg" title="" alt="2.jpg"/></p><p><img src="/media/goods/images/2_20170719161414_628.jpg" title="" alt="2.jpg"/></p><p><img src="/media/goods/images/2_20170719161435_381.jpg" title="" alt="2.jpg"/></p>',
     'sold_nums': 0, 'stored_nums': 0, 'created_time': '2020-08-12T00:11:22.582594',
     'modified_time': '2020-08-12T00:11:22.583364', 'category': 29},
    {'id': 22, 'name': 'JohnnieWalker尊尼获加黑牌威士忌', 'goods_sn': '', 'market_price': 24.0, 'sales_price': 20.0,
     'desc': '', 'goods_front_image': '/media/goods/images/50_P_1448946543091.jpg', 'ship_free': True,
     'goods_desc': '<p><img src="/media/goods/images/2_20170719161405_249.jpg" title="" alt="2.jpg"/></p><p><img src="/media/goods/images/2_20170719161414_628.jpg" title="" alt="2.jpg"/></p><p><img src="/media/goods/images/2_20170719161435_381.jpg" title="" alt="2.jpg"/></p>',
     'sold_nums': 0, 'stored_nums': 0, 'created_time': '2020-08-12T00:11:22.585395',
     'modified_time': '2020-08-12T00:11:22.586160', 'category': 36},
    {'id': 23, 'name': '人头马CLUB特优香槟干邑350ml', 'goods_sn': '', 'market_price': 31.0, 'sales_price': 26.0,
     'desc': '', 'goods_front_image': '/media/goods/images/51_P_1448946466595.jpg', 'ship_free': True,
     'goods_desc': '<p><img src="/media/goods/images/2_20170719161405_249.jpg" title="" alt="2.jpg"/></p><p><img src="/media/goods/images/2_20170719161414_628.jpg" title="" alt="2.jpg"/></p><p><img src="/media/goods/images/2_20170719161435_381.jpg" title="" alt="2.jpg"/></p>',
     'sold_nums': 0, 'stored_nums': 0, 'created_time': '2020-08-12T00:11:22.587672',
     'modified_time': '2020-08-12T00:11:22.588451', 'category': 30},
    {'id': 24, 'name': '张裕干红葡萄酒750ml*6支', 'goods_sn': '', 'market_price': 54.0, 'sales_price': 45.0,
     'desc': '', 'goods_front_image': '/media/goods/images/17_P_1448947102246.jpg', 'ship_free': True,
     'goods_desc': '<p><img src="/media/goods/images/2_20170719161405_249.jpg" title="" alt="2.jpg"/></p><p><img src="/media/goods/images/2_20170719161414_628.jpg" title="" alt="2.jpg"/></p><p><img src="/media/goods/images/2_20170719161435_381.jpg" title="" alt="2.jpg"/></p>',
     'sold_nums': 0, 'stored_nums': 0, 'created_time': '2020-08-12T00:11:22.589878',
     'modified_time': '2020-08-12T00:11:22.590658', 'category': 31},
    {'id': 25, 'name': '原瓶原装进口洋酒烈酒法国云鹿XO白兰地', 'goods_sn': '', 'market_price': 46.0, 'sales_price': 38.0,
     'desc': '', 'goods_front_image': '/media/goods/images/20_P_1448946850602.jpg', 'ship_free': True,
     'goods_desc': '<p><img src="/media/goods/images/2_20170719161405_249.jpg" title="" alt="2.jpg"/></p><p><img src="/media/goods/images/2_20170719161414_628.jpg" title="" alt="2.jpg"/></p><p><img src="/media/goods/images/2_20170719161435_381.jpg" title="" alt="2.jpg"/></p>',
     'sold_nums': 0, 'stored_nums': 0, 'created_time': '2020-08-12T00:11:22.592044',
     'modified_time': '2020-08-12T00:11:22.593015', 'category': 29},
    {'id': 26, 'name': '法国原装进口圣贝克干红葡萄酒750ml', 'goods_sn': '', 'market_price': 82.0, 'sales_price': 68.0,
     'desc': '', 'goods_front_image': '/media/goods/images/19_P_1448946951581.jpg', 'ship_free': True,
     'goods_desc': '<p><img src="/media/goods/images/2_20170719161405_249.jpg" title="" alt="2.jpg"/></p><p><img src="/media/goods/images/2_20170719161414_628.jpg" title="" alt="2.jpg"/></p><p><img src="/media/goods/images/2_20170719161435_381.jpg" title="" alt="2.jpg"/></p>',
     'sold_nums': 0, 'stored_nums': 0, 'created_time': '2020-08-12T00:11:22.594302',
     'modified_time': '2020-08-12T00:11:22.595607', 'category': 25},
    {'id': 27, 'name': '法国百利威干红葡萄酒AOP级6支装', 'goods_sn': '', 'market_price': 67.0, 'sales_price': 56.0,
     'desc': '', 'goods_front_image': '/media/goods/images/18_P_1448947011435.jpg', 'ship_free': True,
     'goods_desc': '<p><img src="/media/goods/images/2_20170719161405_249.jpg" title="" alt="2.jpg"/></p><p><img src="/media/goods/images/2_20170719161414_628.jpg" title="" alt="2.jpg"/></p><p><img src="/media/goods/images/2_20170719161435_381.jpg" title="" alt="2.jpg"/></p>',
     'sold_nums': 0, 'stored_nums': 0, 'created_time': '2020-08-12T00:11:22.597634',
     'modified_time': '2020-08-12T00:11:22.598530', 'category': 25},
    {'id': 28, 'name': '芝华士12年苏格兰威士忌700ml', 'goods_sn': '', 'market_price': 71.0, 'sales_price': 59.0,
     'desc': '', 'goods_front_image': '/media/goods/images/22_P_1448946729629.jpg', 'ship_free': True,
     'goods_desc': '<p><img src="/media/goods/images/2_20170719161405_249.jpg" title="" alt="2.jpg"/></p><p><img src="/media/goods/images/2_20170719161414_628.jpg" title="" alt="2.jpg"/></p><p><img src="/media/goods/images/2_20170719161435_381.jpg" title="" alt="2.jpg"/></p>',
     'sold_nums': 0, 'stored_nums': 0, 'created_time': '2020-08-12T00:11:22.599509',
     'modified_time': '2020-08-12T00:11:22.600334', 'category': 30},
    {'id': 29, 'name': '深蓝伏特加巴维兰利口酒送预调酒', 'goods_sn': '', 'market_price': 31.0, 'sales_price': 18.0,
     'desc': '', 'goods_front_image': '/media/goods/images/45_P_1448946661303.jpg', 'ship_free': True,
     'goods_desc': '<p><img src="/media/goods/images/2_20170719161405_249.jpg" title="" alt="2.jpg"/></p><p><img src="/media/goods/images/2_20170719161414_628.jpg" title="" alt="2.jpg"/></p><p><img src="/media/goods/images/2_20170719161435_381.jpg" title="" alt="2.jpg"/></p>',
     'sold_nums': 0, 'stored_nums': 0, 'created_time': '2020-08-12T00:11:22.601508',
     'modified_time': '2020-08-12T00:11:22.602397', 'category': 36},
    {'id': 30, 'name': '赣南脐橙特级果10斤装', 'goods_sn': '', 'market_price': 43.0, 'sales_price': 36.0, 'desc': '',
     'goods_front_image': '/media/goods/images/32_P_1448948525620.jpg', 'ship_free': True,
     'goods_desc': '<p><img src="/media/goods/images/2_20170719161405_249.jpg" title="" alt="2.jpg"/></p><p><img src="/media/goods/images/2_20170719161414_628.jpg" title="" alt="2.jpg"/></p><p><img src="/media/goods/images/2_20170719161435_381.jpg" title="" alt="2.jpg"/></p>',
     'sold_nums': 0, 'stored_nums': 0, 'created_time': '2020-08-12T00:11:22.603638',
     'modified_time': '2020-08-12T00:11:22.604539', 'category': 62}]
