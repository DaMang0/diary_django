from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from .models import Article

def home(request):
  return HttpResponse("<h1>Testing Git Commit</h1>")

class ArticleListView(ListView):
  model = Article
  context_object_name = 'article_list'
  template_name = 'diary/article_list.html'

class ArticleCreate(CreateView):
  model = Article
  fields = ['title', 'content', 'slug',]
  template_name = 'diary/article_create.html'