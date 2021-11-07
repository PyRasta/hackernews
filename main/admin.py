from django.contrib import admin
from .models import Article, CheckPost, CreateAccount, FindAccount


admin.site.register(Article)
admin.site.register(CreateAccount)
admin.site.register(FindAccount)
admin.site.register(CheckPost)

