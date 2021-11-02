from django.contrib import admin
from .models import Article, CreateAccount, FindAccount


admin.site.register(Article)
admin.site.register(CreateAccount)
admin.site.register(FindAccount)

