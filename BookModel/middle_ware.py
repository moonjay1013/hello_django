from django.utils.deprecation import MiddlewareMixin

from django.shortcuts import render, HttpResponse


class MW1(MiddlewareMixin):
    def process_request(self, request):
        print("mw1  process_request 方法。", id(request))  # 在视图之前执行

    def process_response(self, request, response):  # 基于请求响应
        print("mw1  process_response 方法！", id(request))  # 在视图之后
        return response

    def process_view(self,request, view_func, view_args, view_kwargs):
        print("mw1  process_view 方法！")  # 在视图之前执行 顺序执行
        #return view_func(request)

    def process_exception(self, request, exception):  # 引发错误 才会触发这个方法
        print("mw1  process_exception 方法！")
        # return HttpResponse(exception)  # 返回错误信息
