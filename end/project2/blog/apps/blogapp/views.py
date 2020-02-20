from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.paginator import Paginator,Page
from .models import *
# Create your views here.

def index(request):
    # return HttpResponse('首页')
    ads = Ads.objects.all()
    articles = Article.objects.all()
    #实现一页2篇文章
    paginator = Paginator(articles, 2)
    num = request.GET.get('pagenum', 1)
    print(paginator)
    page = paginator.get_page(num)
    return render(request, 'index.html', {'ads':ads, "page":page})

def detail(request,articleid):
    # return HttpResponse('文章')
    return render(request,'single.html')

def contact(request):
    # return HttpResponse('联系我们')
    return render(request,'contact.html')

def favicon(request):
    return redirect(to='static/favicon.ico')
    # return HttpResponse('调试')