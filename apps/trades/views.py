from datetime import datetime

from rest_framework import viewsets, mixins
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.conf import settings

from apps.utils.custom_permission import IsOwnerOrReadOnly
from apps.utils.alipay import AliPay
from .models import ShoppingCart, OrderGoods
from .models import Order
from .serializers import ShoppingCartSerializer, OrderDetailSerializer
from .serializers import ShoppingCartListSerializer
from .serializers import OrderSerializer


class ShoppingCartViewSet(viewsets.ModelViewSet):
    """
    购物车
    """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    lookup_field = 'goods_id'

    def get_queryset(self):
        return ShoppingCart.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return ShoppingCartListSerializer
        else:
            return ShoppingCartSerializer


class OrderViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin,
                   mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return OrderDetailSerializer
        return OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        order_instance = serializer.save()
        shop_carts = ShoppingCart.objects.filter(user=self.request.user)
        for shop_cart in shop_carts:
            order_goods = OrderGoods()
            order_goods.goods = shop_cart.goods
            order_goods.order = order_instance
            order_goods.nums = shop_cart.nums
            order_goods.save()
            shop_cart.delete()
        return order_instance


class AliPayView(APIView):

    @staticmethod
    def get(request):
        """
        处理支付宝return_url
        :param request:
        :return:
        """
        processed_query = {}
        for key, value in request.GET.items():
            processed_query[key] = value
        ali_sign = processed_query.pop("sign", None)

        alipay = AliPay(
            appid="2016102600761595",
            app_notify_url=settings.NOTIFY_URL,
            app_private_key_path=settings.APP_PRIVATE_KEY_PATH,
            alipay_public_key_path=settings.ALIPAY_PUBLIC_KEY_PATH,
            # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
            debug=True,  # 默认False,
            return_url=settings.RETURN_URL,
        )

        verify = alipay.verify(processed_query, ali_sign)

        # 如果验证通过，将数据同步到数据库，更新订单状
        if verify is True:
            order_sn = processed_query.get("out_trade_no", None)
            pay_status = processed_query.get("trade_status", None)
            trade_no = processed_query.get("trade_no", None)
            exited_orders = Order.objects.filter(order_sn=order_sn)
            for exited_order in exited_orders:
                exited_order.trade_no = trade_no
                exited_order.pay_status = pay_status
                exited_order.pay_time = datetime.now()
                exited_order.save()

            return Response("success")

    @staticmethod
    def post(request):
        """
        处理支付宝notify_url
        :param request:
        :return:
        """
        processed_query = {}
        for key, value in request.POST.items():
            processed_query[key] = value
        ali_sign = processed_query.pop("sign", None)

        alipay = AliPay(
            appid="2016102600761595",
            app_notify_url=settings.NOTIFY_URL,
            app_private_key_path=settings.APP_PRIVATE_KEY_PATH,
            alipay_public_key_path=settings.ALIPAY_PUBLIC_KEY_PATH,
            # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
            debug=True,  # 默认False,
            return_url=settings.RETURN_URL,
        )
        verity = alipay.verify(processed_query, ali_sign)

        # 如果验证通过，将数据同步到数据库，更新订单状
        if verity is True:
            order_sn = processed_query.get("out_trade_no", None)
            pay_status = processed_query.get("trade_status", None)
            trade_no = processed_query.get("trade_no", None)
            exited_orders = Order.objects.filter(order_sn=order_sn)
            for exited_order in exited_orders:
                order_goods = exited_order.order_goods.all()
                for order_good in order_goods:
                    goods = order_good.goods
                    goods.goods_num -= order_good.goods_num
                    goods.save()
                exited_order.trade_no = trade_no
                exited_order.pay_status = pay_status
                exited_order.pay_time = datetime.now()
                exited_order.save()

            return Response("success")
