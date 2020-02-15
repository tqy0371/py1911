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

    def __str__(self):
        return self.title

class Hero(models.Model):
    """
    hero继承了Model 也可以操作数据库
    """
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=6, choices=(('male','男'),('female','女')),default='male')
    content = models.CharField(max_length=20)
    # book是一对多中的外键 on_delete代表删除主表数据时如何做
    book = models.ForeignKey(Book,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class UserManager(models.Manager):

    def deleteByTelePhone(self,tele):
        user = self.get(telephone=tele)
        user.delete()

    def createUser(self,tele):
        user = User()
        user.telephone = tele
        user.save()



class User(models.Model):
    objects = UserManager()
    telephone = models.CharField(max_length=11,null=True,blank=True,verbose_name="手机号码")
    def __str__(self):
        return self.telephone
    class Meta:
        db_table = "用户类"
        ordering = ["telephone"]
        verbose_name = "用户显示模型类a"
        verbose_name_plural = "用户模型类s"


class Account(models.Model):
    username = models.CharField(max_length=20,verbose_name="用户名")
    password = models.CharField(max_length=20,verbose_name="密码")
    regist_date = models.DateField(auto_now_add=True,verbose_name="注册日期")


class Concact(models.Model):
    telephone = models.CharField(max_length=11,verbose_name="手机号")
    email = models.EmailField(default="1980739637@qq.com")
    account = models.OneToOneField(Account,on_delete=models.CASCADE,related_name='con')

class Article(models.Model):
    title = models.CharField(max_length=20,verbose_name="标题")
    sumary = models.TextField(verbose_name="正文")

class Tag(models.Model):
    name = models.CharField(max_length=20,verbose_name="标签名")
    articles = models.ManyToManyField(Article)