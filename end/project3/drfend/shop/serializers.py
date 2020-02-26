from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    """
    编写针对Category的序列化类
    本类指明了Category的序列化细节
    需要继承ModelSerializer才可以针对模型进行序列化
    在Meta类中model知名序列化的模型是谁 field指明序列化的字段
    """
    # goods = serializers.StringRelatedField(many=True)
    # goods = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    goods = serializers.HyperlinkedRelatedField(view_name='good-detail',read_only=True,many=True)
    class Meta:
        model = Category
        fields = ('name','goods')

class GoodSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source="category.name",read_only=True)
    class Meta:
        model = Good
        fields = ('name','desc','category')