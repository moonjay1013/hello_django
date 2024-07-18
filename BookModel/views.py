from django.shortcuts import render, redirect
from BookModel import models
from django.http import HttpResponse


# Create your views here.
def add_book(request):
    #  获取出版社对象
    pub_obj = models.Publish.objects.filter(pk=1).first()
    #  给书籍的出版社属性publish传出版社对象
    book = models.Book.objects.create(title="冲灵剑法", price=200, pub_date="2024-7-13", publish=pub_obj.id)
    print(book, type(book))
    return HttpResponse("<p>" + str(book) + ", 数据添加成功！</p>")


def add_b2a(request):
    #  获取作者对象
    chong = models.Author.objects.filter(name="令狐冲").first()
    ying = models.Author.objects.filter(name="任盈盈").first()
    #  获取书籍对象
    book = models.Book.objects.filter(title="冲灵剑法").first()
    book.authors.add(chong, ying)
    return HttpResponse("<p>成功添加</p>")


def association_set(request):
    # ying = models.Author.objects.filter(name="任盈盈").first()
    # book = models.Book.objects.filter(title="冲灵剑法").first()
    # ying.book_set.add(book)  # 影响 book_authors 表

    # 创建一个新的对象，并同时将它添加到关联对象集之中。
    pub = models.Publish.objects.filter(name="明教出版社").first()
    wo = models.Author.objects.filter(name="任我行").first()
    book = wo.book_set.create(title="吸星大法", price=300, pub_date="1999-9-19", publish=pub.pk)
    # 会影响book表和book2author表
    print(book, type(book))
    return HttpResponse("ok")


def one2many_find(request):
    # book = models.Book.objects.filter(pk=1).first()
    # res = book.publish.city
    # print(res, type(res))

    pub = models.Publish.objects.filter(name="明教出版社").first()
    res = pub.book_set.all()
    res_li = []
    for i in res:
        res_li.append(i.title)
        print(i.title)
    return HttpResponse(res_li)


def one2one_find(request):
    # author = models.Author.objects.filter(name="令狐冲").first()
    # res = author.au_detail.tel

    addr = models.AuthorDetail.objects.filter(addr="黑木崖").first()
    res = addr.author.name
    print(res, type(res))

    return HttpResponse(res)


def many2many_find(request):
    # book = models.Book.objects.filter(title="吸星大法").first()
    # res = book.authors.all()
    # for i in res:
    #     print(i.name, i.au_detail.tel)

    author = models.Author.objects.filter(name="任我行").first()
    res = author.book_set.all()
    for i in res:
        print(i.title)
    return HttpResponse("ok")


def cross_table_find(request):
    # one2many
    # res = models.Book.objects.filter(publish__name="华山出版社").values_list("title", "price")  # 正向
    # res = models.Publish.objects.filter(name="华山出版社").values_list("book__title", "book__price")  # 反向

    # many2many
    # res = models.Book.objects.filter(authors__name="任我行").values_list("title")
    # res = models.Author.objects.filter(name="任我行").values_list("book__title")

    # one2one
    # res = models.Author.objects.filter(name="任我行").values_list("au_detail__tel")
    res = models.AuthorDetail.objects.filter(author__name="任我行").values_list("tel")
    return HttpResponse(res)


from django.db.models import Avg, Max, Min, Count, Sum


def use_aggregate(request):
    # res = models.Book.objects.aggregate(Avg("price"))
    # print(res)  # {'price__avg': Decimal('250.000000')}
    # return HttpResponse(res["price__avg"])  # 250.000000

    # 计算所有图书的数量、最贵价格和最便宜价格：
    res = models.Book.objects.aggregate(c=Count("id"), max=Max("price"), min=Min("price"))
    print(res)  # {'c': 2, 'max': Decimal('300.00'), 'min': Decimal('200.00')}
    return HttpResponse("Count: " + str(res["c"]) + "Max: " + str(res["max"]) + "Min: " + str(res["min"]))


def use_annotate(request):
    # 每一个出版社的最便宜的书的价格
    # res = models.Publish.objects.values("name").annotate(in_price=Min("book__price"))
    # res type -- QuerySet
    # <[{'name': '华山出版社', 'in_price': Decimal('200.00')}, {'name': '明教出版社', 'in_price': Decimal('300.00')}]>

    # 统计每一本书的作者个数
    # res = models.Book.objects.annotate(c=Count("authors__name")).values("title", "c")
    # <QuerySet [{'title': '冲灵剑法', 'c': 2}, {'title': '吸星大法', 'c': 1}]>

    # 统计每一本以 ** "冲" ** 开头的书籍的作者个数：
    # res = models.Book.objects.filter(title__startswith="冲").annotate(c=Count("authors__name")).values("title", "c")
    # <QuerySet [{'title': '冲灵剑法', 'c': 2}]>

    # 统计不止一个作者的图书名称
    # res = models.Book.objects.annotate(c=Count("authors__name")).filter(c__gt=1).values("title", "c")
    # <QuerySet [{'title': '冲灵剑法', 'c': 2}]>

    # 根据一本图书作者数量的多少对查询集 QuerySet 进行降序排序
    # res = models.Book.objects.annotate(c=Count("authors__name")).order_by("-c").values("title", "c")
    # <QuerySet [{'title': '冲灵剑法', 'c': 2}, {'title': '吸星大法', 'c': 1}]>

    # 查询各个作者出的书的总价格:
    res = models.Author.objects.annotate(all=Sum("book__price")).values("name", "all")
    # <QuerySet [{'name': '令狐冲', 'all': Decimal('200.00')},
    # {'name': '任我行', 'all': Decimal('300.00')}, {'name': '任盈盈', 'all': Decimal('200.00')}]>
    return HttpResponse(res)


from django.db.models import F


def use_f(request):
    # 查询工资大于年龄的人
    # res = models.Emp.objects.filter(salary__gt=F("age")).values("name", "age")
    # <QuerySet [{'name': '令狐冲', 'age': 24}, {'name': '任盈盈', 'age': 18}, {'name': '任我行', 'age': 56},
    # {'name': '岳灵珊', 'age': 19}, {'name': '小龙女', 'age': 20}]>

    # 将每一本书的价格提高100元
    res = models.Book.objects.update(price=F("price") + 100)
    # res为受影响行数
    return HttpResponse(res)


from django.db.models import Q


def use_q(request):
    # 查询价格大于 350 或者名称以“冲”开头的书籍的名称和价格
    res = models.Book.objects.filter(Q(price__gt=350) | Q(title__startswith="冲")).values("title", "price")
    # <QuerySet [{'title': '冲灵剑法', 'price': Decimal('300.00')}, {'title': '吸星大法', 'price': Decimal('400.00')}]>

    # 查询以"法"结尾或者不是 2010 年 10 月份的书籍:
    # res = models.Book.objects.filter(Q(title__endswith="法") | ~Q(Q(pub_date__year=2010) & Q(pub_date__month=10)))
    # <QuerySet [<Book: Book object (1)>, <Book: Book object (7)>]>

    # 查询出版日期是 2004 或者 1999 年，并且书名中包含有"大"的书籍
    # res = models.Book.objects.filter(Q(pub_date__year=2004) | Q(pub_date__year=1999), title__contains="大")
    # <QuerySet [<Book: Book object (7)>]>
    return HttpResponse(res)


from BookModel.my_forms import EmpForm


# Create your views here.
def add_emp(request):
    if request.method == "GET":
        form = EmpForm()  # 初始化form对象
        return render(request, "add_emp.html", {"form":form})
    else:
        form = EmpForm(request.POST)  # 将数据传给form对象
        if form.is_valid():  # 进行校验
            data = form.cleaned_data
            data.pop("r_salary")
            models.Emp.objects.create(**data)
            return redirect("/index/")
        else:  # 校验失败
            clear_errors = form.errors.get("__all__")  # 获取全局钩子错误信息
            return render(request, "add_emp.html", {"form": form, "clear_errors": clear_errors})
