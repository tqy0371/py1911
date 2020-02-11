from django.db import models

# Create your models here.
# 在此处编写数据模型类
# 每一张表就是一个模型类
# 有了orm之后就能定义出表对应的模型类
# 通过操作模型类去操作数据库 不用写sql语句

class Book(models.Model):
    """
    book继承了Model类  因为Model类具有操作数据库的功能
    """
    title = models.CharField(max_length=20)
    price = models.FloatField(default=0)
    pub_data = models.DateField(default="1983-06-01")

class Hero(models.Model):
    """
    hero继承了Model 也可以操作数据库
    """
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=6, choices=(('male','男'),('female','女')),default='male')
    content = models.CharField(max_length=20)
    # book是一对多中的外键 on_delete代表删除主表数据时如何做
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
