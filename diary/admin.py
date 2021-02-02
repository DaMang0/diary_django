from django.contrib import admin
from .models import Article, RichTextArticle
# Register your models here.
admin.site.register(Article)
admin.site.register(RichTextArticle)