from django.shortcuts import render, redirect

from CookieModel import models


# Create your views here.
def login_common(request):
    if request.method == "GET":
        return render(request, "login.html")
    username = request.POST.get("username")
    password = request.POST.get("pwd")

    user_obj = models.UserInfo.objects.filter(username=username, password=password).first()
    print(user_obj.username)
    return user_obj


def login(request):
    user_obj = login_common(request)

    if not user_obj:
        return redirect("/login/")
    else:
        rep = redirect("/index/")
        rep.set_cookie("is_login", True)
        return rep


def index(request):
    print(request.COOKIES.get('is_login'))
    status = request.COOKIES.get('is_login')  # 收到浏览器的再次请求,判断浏览器携带的cookie是不是登录成功的时候响应的 cookie
    if not status:
        return redirect('/login/')
    return render(request, "index_cookie.html")


def logout(request):
    rep = redirect('/login/')
    rep.delete_cookie("is_login")
    return rep  # 点击注销后执行,删除cookie,不再保存用户状态，并弹到登录页面


def order(request):
    print(request.COOKIES.get('is_login'))
    status = request.COOKIES.get('is_login')
    if not status:
        return redirect('/login/')
    return render(request, "order.html")


def s_login(request):
    user_obj = login_common(request)

    if not user_obj:
            return redirect("/session_login/")
    else:
        request.session['is_login'] = True
        request.session['user1'] = request.POST.get('username')
        return redirect("/s_index/")


def s_index(request):
    status = request.session.get('is_login')
    if not status:
        return redirect('/session_login/')
    return render(request, "s_index.html")


def s_logout(request):
    # del request.session["is_login"] # 删除session_data里的一组键值对
    request.session.flush()  # 删除一条记录包括(session_key session_data expire_date)三个字段
    return redirect('/session_login/')
