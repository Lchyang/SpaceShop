from django.urls import path, include
from rest_framework.routers import DefaultRouter

from goods import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
# router.register(r'goods', views.GoodsView)
# router.register(r'categories', views.CategoriesListViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('goods/', views.GoodsListView.as_view()),
    path('goods/<int:pk>/', views.GoodDetailView.as_view()),
    # path('categories/', views.CategoriesListCreateView.as_view()),
    # path('categories/<int:pk>/', views.CategoriesRetrieveView.as_view()),
]
