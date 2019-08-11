import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    """测试首页"""
    return render(request,'base.html')

def hello(request):
    """测试用例"""
    return HttpResponse(u'您好！欢迎搭建系统平台成功！')

def home(request):
    """旅行首页"""
    return render(request,'travel/home.html')

def picture(request):
    """彝家风光部分"""
    return render(request,'travel/picture.html')

def detail(request):
    """详情页"""
    return render(request,'travel/detail.html')

def wechart(request):
    """微信本地测试"""
    data = {
        'name':'xieqiang',
        'address':'西昌',
    }
    return HttpResponse(json.dumps(data), content_type="application/json")