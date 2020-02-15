from django.contrib import admin
from django.contrib.admin import ModelAdmin
# 定义后端显示界面
# Register your models here.
# django自带的后台管理操作需要在此实现

# 注册自己需要管理的模型

from .models import Book, Hero, User, Account, Concact
class HeroInline(admin.StackedInline):
    """
    定义关联类
    """
    model = Hero
    extra = 5

class BookAdmin(ModelAdmin):
    """
    定义模型管理类
    通过该类可以修改后台页面
    """
    list_display = ('title', 'price', 'pub_data')
    # list_per_page = 1
    search_fields = ('title', 'price')
    list_filter = ('title',)
    inlines = [HeroInline]

class HeroAdmin(ModelAdmin):
    list_display = ('name', 'gender', 'content', 'book')
    search_fields = ('gender',)
    list_filter = ('gender',)

admin.site.register (Book, BookAdmin)
admin.site.register (Hero, HeroAdmin)
admin.site.register (User)
admin.site.register (Account)
admin.site.register (Concact)