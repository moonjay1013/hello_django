"""
URL configuration for hello_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views, testdb, form
from BookModel import views as book_views
from CookieModel import views as cookie_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("hello/", views.hello, name="hello"),
    path("", views.index, name="index"),
    path("show_img/", views.show_img, name="show_img"),
    path("test_add/", testdb.test_add, name="test_add"),
    path("test_get/", testdb.test_get, name="test_get"),
    path("test_update/", testdb.test_update, name="test_update"),
    path("test_del/", testdb.test_del, name="test_del"),

    path("search_form/", form.search_form, name="search_form"),
    path("search/", form.search, name="search"),
    path("post_form/", form.post_form, name="post_form"),

    path("add_book/", book_views.add_book, name="add_book"),
    path("add_book2author/", book_views.add_b2a, name="add_b2a"),
    path("use_set/", book_views.association_set, name="association_set"),
    path("find1/", book_views.one2many_find, name="one2many_find"),
    path("find2/", book_views.one2one_find, name="one2one_find"),
    path("find3/", book_views.many2many_find, name="many2many_find"),
    path("find4/", book_views.cross_table_find),

    path("use_aggregate/", book_views.use_aggregate),
    path("use_annotate/", book_views.use_annotate),

    path("use_f/", book_views.use_f),
    path("use_q/", book_views.use_q),

    path('add_emp/', book_views.add_emp),

    path('login/', cookie_views.login),
    path("index/", cookie_views.index),
    path('logout/', cookie_views.logout),
    path('order/', cookie_views.order),

    path('session_login/', cookie_views.s_login),
    path('s_index/', cookie_views.s_index),
    path('s_logout/', cookie_views.s_logout),

    path("login_class/", views.Login.as_view()),
]
