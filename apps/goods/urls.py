from django.conf.urls import include, re_path
from django.urls import path
from rest_framework.routers import DefaultRouter

from goods import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'goods', views.GoodsView)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]
