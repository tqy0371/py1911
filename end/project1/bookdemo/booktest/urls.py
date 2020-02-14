# 引入路由绑定函数
from django.conf.urls import url
from . import views

app_name = 'booktest'
# 每一个路由文件中必须编写一个路由列表
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'detail/(\d+)/', views.detail, name='detail'),
]