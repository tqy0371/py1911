from django.contrib import admin

# Register your models here.
# django自带的后天管理操作需要在此实现

# 注册自己需要管理的模型

from .models import Book,Hero
admin.site.register(Book)
admin.site.register(Hero)