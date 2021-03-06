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
from django.urls import path
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token
import xadmin

sub_urlpatterns = [
    path('goods/', include('goods.urls'), name='goods'),
    path('users/', include('users.urls'), name='users'),
    path('actions/', include('user_actions.urls'), name='actions'),
    path('trades/', include('trades.urls'), name='trades'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('xadmin/', xadmin.site.urls),
    path('jwt-login/', obtain_jwt_token),
    path('docs/', include_docs_urls(title='SpaceShop')),
    url('', include('social_django.urls', namespace='social'))

]

# 静态文件配置，debug=True时才能生效
urlpatterns = sub_urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
