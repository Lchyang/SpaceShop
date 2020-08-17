from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'code', views.VerifyMobileViewSet)
router.register(r'registor', views.RegisterViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]
