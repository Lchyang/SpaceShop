from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter

from users import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'code', views.VerifyMobileViewSet, basename='code')
router.register(r'register', views.RegisterViewSet, basename='register')
router.register(r'center', views.UserCenterViewSet, basename='center')

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]
