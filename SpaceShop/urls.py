"""SpaceShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include, url
from django.conf import settings
from django.views.generic import TemplateView
from django.conf.urls.static import static
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

# 配置生成文档
schema_view = get_schema_view(
    title="SpaceShop",
    description="API for all goods",
    version="1.0.0",
)

sub_urlpatterns = [
    path('', include('goods.urls'), name='goods'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    # rest_framework 自带docs
    re_path(r'^docs/', include_docs_urls(title='SpaceShop')),
    # swagger UI 暂时不用
    path('openapi-schema', schema_view, name='openapi-schema'),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
]

# 静态文件配置，debug=True时才能生效
urlpatterns = sub_urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
