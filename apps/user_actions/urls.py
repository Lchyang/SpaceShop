from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter

from user_actions import views

router = DefaultRouter()
router.register(r'favorite', views.UserFavViewSet, basename='favorite')

urlpatterns = [
    path('', include(router.urls)),
]
