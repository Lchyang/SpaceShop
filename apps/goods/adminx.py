import xadmin
from goods import models


class GoodsAdmin(object):
    # 显示的字段名称
    list_display = ['id', 'name', 'category', 'sales_price', 'created_time']

    # 搜索时可输入的字段内容
    search_fields = ['name']

    # 点击id可进入详细界面进行编辑（默认的）
    list_display_links = ('id', 'name')

    # 可编辑的列名
    list_editable = ['name', 'category']
    list_filter = ['name', 'sales_price']

    # 每页显示多少条
    list_per_page = 20

    # 根据id排序
    ordering = ('id',)
    # 设置只读字段　
    readonly_fields = ('goods_sn', 'created_time', 'modified_time', 'sold_nums')

    # 显示本条数据的所有信息
    # show_detail_fields = ['asset_name']
    class GoodsImagesInline(object):
        model = models.GoodImages
        exclude = ["created_time", 'modified_time']
        extra = 1
        style = 'tab'

    inlines = [GoodsImagesInline]


class GoodCategoriesAdmin(object):
    list_display = ["name", "category_type", "parent_category"]
    list_filter = ["category_type", "parent_category", "name"]
    search_fields = ['name', 'category_type']


xadmin.site.register(models.Goods, GoodsAdmin)
xadmin.site.register(models.GoodCategories, GoodCategoriesAdmin)
