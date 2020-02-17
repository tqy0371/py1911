from django.db import models

# Create your models here.

class Question(models.Model):
    """
    投票问题类
    """
    title = models.CharField(max_length=50, verbose_name='投票问题')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '投票表'
        verbose_name_plural = verbose_name
        ordering = ['-create_time']


class Choice(models.Model):
    """
    投票选项类
    """
    content = models.CharField(max_length=50, verbose_name='选项')
    votes = models.PositiveIntegerField(verbose_name='得票数')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    question = models.ForeignKey(Question,on_delete=models.CASCADE,related_name='choice',verbose_name="所属问题")
    def __str__(self):
        return self.content

    class Meta:
        verbose_name = '选项表'
        verbose_name_plural = verbose_name
        ordering = ['-create_time']