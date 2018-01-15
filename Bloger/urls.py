from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve  # 媒体文件
from rest_framework.documentation import include_docs_urls

from Bloger.settings import MEDIA_ROOT
from common.base_view import JWTTokenView

urlpatterns = [
    # admin 后台
    url(r'^admin/', admin.site.urls),

    # docs 下的文档路由
    url(r'^docs/', include_docs_urls(title='博客系统')),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # 登录，到时候得自定义这个
    url(r'^login/', JWTTokenView.as_view()),

    # 上传的文件配置
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),

    url(r'^users/', include('users.urls', namespace='users'))
]
