"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.urls import path, include, re_path
from django.views import static

from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.documentation import include_docs_urls

from common.urls import urlpatterns as common_urls
from analysis.urls import urlpatterns as analysis_urls
from polls.urls import urlpatterns as polls_urls
from checkin.urls import urlpatterns as checkin_urls

API_TITLE = '接口文档'
API_DESCRIPTION = '我的Api服务'

urlpatterns = [
    path(r'super/', admin.site.urls),
    # path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path(r'^api-token-auth/', obtain_auth_token),   # drf 自带的 token 认证模式
    path(r'common/', include(common_urls)),  # jwt 的认证接口
    path(r'analysis/', include(analysis_urls)),
    path(r'polls/', include(polls_urls)),
    path(r'wx/', include(checkin_urls)),
    path(r'docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION, authentication_classes=[], permission_classes=[])),
    re_path(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT}, name='static'),
]