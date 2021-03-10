from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Article, RichTextArticle
from django.urls import reverse_lazy
from datetime import date
class ArticleIndex(TemplateView):
  model = Article
  template_name = 'diary/index.html'

  def get_context_data(self, **kwargs):

    today = date.today()
    context = super().get_context_data(**kwargs)
    context['year'] = today.year
    context['month'] = today.month
    context['day'] = today.day
    return context

class ArticleListView(ListView):
  model = Article
  context_object_name = 'article_list'
  template_name = 'diary/list.html'
  queryset = Article.objects.all().order_by('-pub_date')
  # queryset = Article.objects.all().order_by('-modified')

class ArticleCreate(CreateView):
  model = Article
  fields = ['title', 'body']
  template_name = 'diary/create.html'

class ArticleDetail(DetailView):
  model = Article
  template_name = 'diary/detail.html'

  def get_object(self):
    slug_ = self.kwargs.get("slug")
    return get_object_or_404(Article, slug=slug_)

class ArticleDelete(DeleteView):
  model = Article
  success_url = reverse_lazy('article:list')
  template_name = 'diary/delete.html'

  def get_object(self):
    slug_ = self.kwargs.get("slug")
    return get_object_or_404(Article, slug=slug_)

class ArticleUpdate(UpdateView):
  model = Article
  fields = ['title', 'body']
  template_name = "diary/update.html"

  def get_object(self):
    slug_ = self.kwargs.get("slug")
    return get_object_or_404(Article, slug=slug_)

class Test(ListView):
  model = RichTextArticle
  context_object_name = 'richTextArticle_list'
  template_name = 'diary/test_article.html'