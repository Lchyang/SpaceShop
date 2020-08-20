from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter

from trades import views

router = DefaultRouter()
router.register(r'shopcart', views.ShoppingCartViewSet, basename='shopcart')

urlpatterns = [
    path('', include(router.urls)),
]