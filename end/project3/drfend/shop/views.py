from rest_framework import viewsets
from .models import *
from .serializers import *

class CategoryViewSets(viewsets.ModelViewSet):
    """
    分类视图
    继承ModelViewSet之后拥有GET POST PUT DELETE等HTTP动词操作
    queryset指明需要操作的模型列表
    serializer_class指明序列化类
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class GoodViewSets(viewsets.ModelViewSet):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer