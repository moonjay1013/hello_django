from django.db import models


# Create your models here.
class Book(models.Model):
    id = models.AutoField(primary_key=True)  # id 会自动创建,可以手动写入
    title = models.CharField(max_length=32)  # 书籍名称
    price = models.DecimalField(max_digits=5, decimal_places=2)  # 书籍价格
    publish = models.ForeignKey("Publish", on_delete=models.CASCADE)  # 出版社名称
    pub_date = models.DateField()  # 出版时间
    authors = models.ManyToManyField("Author")  # 会自动生成 book_authors 表


class Publish(models.Model):
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=64)
    email = models.EmailField()


class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.SmallIntegerField()
    au_detail = models.OneToOneField("AuthorDetail", on_delete=models.CASCADE)


class AuthorDetail(models.Model):
    gender_choices = (
        (0, "女"),
        (1, "男"),
        (2, "保密"),
    )
    gender = models.SmallIntegerField(choices=gender_choices)
    tel = models.CharField(max_length=32)
    addr = models.CharField(max_length=64)
    birthday = models.DateField()


# ------------------------------------------------------------
class Emp(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    dep = models.CharField(max_length=32)
    province = models.CharField(max_length=32)


class Emps(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    dep = models.ForeignKey("Dep", on_delete=models.CASCADE)
    province = models.CharField(max_length=32)


class Dep(models.Model):
    title = models.CharField(max_length=32)
