from django.contrib import admin
from BookModel.models import Book, Publish, Author, AuthorDetail

# Register your models here.
admin.site.register([Book, Publish, Author, AuthorDetail])
