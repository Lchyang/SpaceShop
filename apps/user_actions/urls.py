from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter

from user_actions import views

router = DefaultRouter()
# TODO url 里面的name都有什么用？spacename basename name
router.register(r'favorite', views.UserFavViewSet, basename='favorite')

urlpatterns = [
    path('', include(router.urls)),
]
