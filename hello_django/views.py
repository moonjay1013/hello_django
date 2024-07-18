from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse("Hello Django!")


def index(request):
    import datetime
    now = datetime.datetime.now()

    views_list = ["1 元素", "2 Python", "3 Django"]

    safe_str = "<a href='https://www.runoob.com/'>点击跳转-菜鸟教程</a>"

    if_else_num = 88

    context = {
        'replace_text': 'Hello Django!!',
        'replace_list': views_list,
        "time": now,
        "safe_str": safe_str,
        "if_else_num": if_else_num,
    }

    return render(request, 'index.html', context)


def show_img(request):
    name = "profile IMG"
    return render(request, 'show_img.html', {"name": name})


from django.views import View


class Login(View):
    def get(self,request):
        return HttpResponse("GET 方法")

    def post(self,request):
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        if user == "runoob" and pwd == "123456":
            return HttpResponse("POST 方法")
        else:
            return HttpResponse("POST 方法 1")
