from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter

from trades import views

router = DefaultRouter()
router.register(r'shopcart', views.ShoppingCartViewSet, basename='shopcart')
router.register(r'order', views.OrderViewSet, basename='order')
router.register(r'alipay', views.OrderViewSet, basename='alipay')

urlpatterns = [
    path('', include(router.urls)),
]
