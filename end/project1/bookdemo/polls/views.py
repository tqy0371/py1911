from django.shortcuts import render,reverse,redirect
from .models import Question,Choice
# Create your views here.
from django.http import HttpResponse
from . import *

def index(request):
    questions = Question.objects.all()
    return render(request,'polls/index.html',{'questions':questions})
    return HttpResponse('首页')

def detail(request,qid):

    if request.method == "GET":
        try:
            question = Question.objects.get(id=qid)
            return render(request,'polls/detail.html',{'question':question})
        except Exception as e:
            print(e)
            return HttpResponse('问题不合法')

        # return HttpResponse('详情页'+qid)
    elif request.method == "POST":
        choiceid = request.POST.get('num')
        try:
            choice = Choice.objects.get(id=choiceid)
            choice.votes+=1
            choice.save()
            url = reverse("polls:result",args=(qid,))
            return redirect(to=url)
        except:
            return HttpResponse('选项不合法')


def result(request,qid):
    try:
        question = Question.objects.get(id=qid)
        return render(request,"polls/result.html",{'question':question})
    except:
        return HttpResponse('不合法')