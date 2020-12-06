from django.shortcuts import render, HttpResponseRedirect
from oj import models as oj_models
from login import models as login_models
# from captcha.models import CaptchaStore
# from captcha.helpers import captcha_image_url


def index(request):
    """登录页面"""
    # 验证码生成
    # hashkey = CaptchaStore.generate_key()
    # imgage_url = captcha_image_url(hashkey)
    return render(request, 'login/index.html')


def login_action(request):
    if request.session.get('is_login', None):
        # 不允许重复登录
        return HttpResponseRedirect('/questions/all')
    # 验证码生成
    # hashkey = CaptchaStore.generate_key()
    # imgage_url = captcha_image_url(hashkey)
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        # 用户输入的验证码
        # vcode = request.POST.get('vcode')
        # # 验证码在数据库中对应的hashkey值，用于查找正确的验证码
        # vcode_key = request.POST.get('hashkey')
        # # 验证查询数据库生成正确的码
        # captcha = CaptchaStore.objects.get(hashkey=vcode_key)
        if username and password:
            username = username.strip()
            # 账号密码验证
            try:
                user = login_models.Student.objects.get(student_number=username)
                if user.password == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.student_number
                    return HttpResponseRedirect('/questions/all')
                    # 将用户输入的验证码小写后与数据库查询的response值对比：
                    # vcode = vcode.lower()
                    # if vcode == captcha.response:
                    #     request.session['is_login'] = True
                    #     request.session['user_id'] = user.student_number
                    #     next = request.POST.get('next', None)
                    #     if next == 'None':
                    #         return render(request, 'oj/question_all.html',
                    #                       {'questions': questions})
                    #     elif next:
                    #         return HttpResponseRedirect(next)
                    #     else:
                    #         return render(request, 'oj/question_all.html',
                    #                       {'questions': questions})
                    # else:
                    #     message = '验证码错误'
                else:
                    message = '密码错误！'
            except:
                message = '学号不存在！'
            return render(request, 'login/index.html', locals())


def register_page(request):
    return render(request, 'login/register.html', locals())


def register_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', None).strip()
        password = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)
        if username and password and password2:
            try:
                student = login_models.Student.objects.get(student_number=username)
                message = '该学号已注册'
                return render(request, 'login/register.html', locals())
            except:
                if password != password2:
                    message = '两次密码输入不一致'
                    return render(request, 'login/register.html', locals())
                else:
                    student = login_models.Student.objects.create(
                        student_number=username, password=password)
                    # hashkey = CaptchaStore.generate_key()
                    # imgage_url = captcha_image_url(hashkey)
                    return render(request, 'login/index.html', locals())
    return render(request, 'login/register.html', locals())


def logout(request):
    """退出登录"""
    request.session.flush()  # 删除当前的会话数据和会话cookie。
    return HttpResponseRedirect('/questions/all')




