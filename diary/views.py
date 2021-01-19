from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Article
from django.urls import reverse_lazy

class ArticleListView(ListView):
  model = Article
  context_object_name = 'article_list'
  template_name = 'diary/article_list.html'

class ArticleCreate(CreateView):
  model = Article
  fields = ['title', 'content']
  template_name = 'diary/article_create.html'

class ArticleDetail(DetailView):
  model = Article
  template_name = 'diary/article_detail.html'

  def get_object(self):
    slug_ = self.kwargs.get("slug")
    return get_object_or_404(Article, slug=slug_)

class ArticleDelete(DeleteView):
  model = Article
  success_url = reverse_lazy('article-list')
  template_name = 'diary/article_delete.html'

  def get_object(self):
    slug_ = self.kwargs.get("slug")
    return get_object_or_404(Article, slug=slug_)

class ArticleUpdate(UpdateView):
  model = Article
  fields = ['title', 'content']
  template_name = "diary/article_update_form.html"

  def get_object(self):
    slug_ = self.kwargs.get("slug")
    return get_object_or_404(Article, slug=slug_)