from django.shortcuts import render
from django.template import loader
from .models import Book,Hero

# Create your views here.

from django.http import HttpResponse
def index(requests):
    # return HttpResponse("这里是首页")
    # 获取模板
    # template = loader.get_template('index.html')
    # 渲染模板数据
    books = Book.objects.all()
    # context = {"books":books}
    # result = template.render(context)
    # 将渲染结果使用httpresponse返回
    # return HttpResponse(result)
    return render(requests,'index.html',{'books':books})

def about(requsets):
    return HttpResponse("这里是关于页面")

def detail(request,bookid):
    # template = loader.get_template('detail.html')
    book = Book.objects.get(id=bookid)
    # context = {"book":book}
    # result = template.render(context)
    # return HttpResponse(result)
    return render(request,'detail.html',{'book':book})

# 使用Django模板

