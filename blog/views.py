from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import *
from django.core import serializers
from . import models

def index(request):
    return render(request, 'blog/index.html')

@csrf_exempt
def login(request):
    if request.method == "POST":
        username = request.POST.get('user', None)
        password = request.POST.get('password', None)
        if username and password:
            username = username.strip()
            try:
                user = models.UserInfo.objects.get(user_name=username)
                if user.user_pwd == password:
                    response = JsonResponse({'status': 0, 'message': "登录成功"})
                    response.set_cookie('user', username)
                    return response
                else:
                    return JsonResponse({'status': 1, 'message': "密码不正确"})
            except:
                    return JsonResponse({'status': 1, 'message': "此用户不存在,请注册"})
        else:
            return JsonResponse({'status': 1, 'message': "用户名、密码不能为空"})
    else:
        return JsonResponse({'status': 1, 'message': "请求出现错误"})

def register(request):
    return render(request, 'blog/register.html')

@csrf_exempt
def register1(request):
    if request.method == "POST":
        username = request.POST.get('user', None)
        password = request.POST.get('password', None)
        if username and password:
            username = username.strip()
            try:
                user = models.UserInfo.objects.get(user_name=username)
                return JsonResponse({'status': 1, 'message': "此用户已存在"})
            except:
                models.UserInfo.objects.create(user_name=username, user_pwd=password)
                response = JsonResponse({'status': 0, 'message': "注册成功"})
                response.set_cookie('user', username)
                return  response
        else:
            return JsonResponse({'status': 1, 'message': "用户名、密码不能为空"})
    else:
        return JsonResponse({'status': 1, 'message': "请求出现错误"})

def person(request):
    return render(request, 'blog/person.html')

def query(request):
    cookie = request.COOKIES.get('user', None)
    if not cookie:
        print(2)
        return JsonResponse({'status': 1, 'message': "请先登录"})
    result = serializers.serialize("json", models.BlogInfo.objects.filter(user_id=cookie))
    if result:
        return render(request, 'blog/query.html', {'result': eval(result)})
    else:
        return render(request, 'blog/query.html', {'result': eval(result)})



@csrf_exempt
def write(request):
    if request.method == "POST":
        cookie = request.COOKIES.get('user', None)
        if not cookie:
            return JsonResponse({'status': 1, 'message': "请先登录"})
        date = request.POST.get('date', None)
        content = request.POST.get('content', None)
        number = request.POST.get('number', None)
        type = request.POST.get('type', None)
        if date and number and type:

            # models.BlogInfo.objects.create(date=date, content=content, number=number, type=type, user_id=cookie)
            # return JsonResponse({'status': 0, 'message': "保存成功"})
            try:
                models.BlogInfo.objects.create(date=date, content=content, number=number, type=type, user_id=cookie)
                return JsonResponse({'status': 0, 'message': "保存成功"})
            except:
                return JsonResponse({'status': 1, 'message': "保存失败"})

        else:
            return JsonResponse({'status': 1, 'message': "记账不能为空"})
    else:
        return JsonResponse({'status': 1, 'message': "请求出现错误"})

def income(request):
    return render(request, 'blog/income.html')

