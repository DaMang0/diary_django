from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Article, RichTextArticle, Category
from django.urls import reverse_lazy, reverse
from datetime import date
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
class Index(TemplateView):
  model = Article
  template_name = 'diary/index.html'

  def get_context_data(self, **kwargs):
    today = date.today()
    context = super().get_context_data(**kwargs)
    context['year'] = today.year
    context['month'] = today.month
    context['day'] = today.day
    return context

class List(LoginRequiredMixin, ListView):
  model = Article
  context_object_name = 'article_list'
  template_name = 'diary/list.html'
  paginate_by = 10
  
  
  def get_queryset(self):
    return Article.objects.filter(user=self.request.user).order_by('-modified')

class Detail(LoginRequiredMixin, DetailView):
  model = Article
  template_name = 'diary/detail.html'

  def get_context_data(self, *, object_list=None, **kwargs):
    user = self.request.user
    context = super().get_context_data(**kwargs)
    context['recent_articles'] = Article.objects.filter(user=user).order_by('-modified')[:3]
    return context

  def get_object(self):
    slug_ = self.kwargs.get("slug")
    return get_object_or_404(Article, slug=slug_)
class Create(LoginRequiredMixin, CreateView):
  model = Article
  fields = ['title', 'body', 'category']
  template_name = 'diary/create.html'
  success_url = reverse_lazy('article:list')

  def form_valid(self, form):
      obj = form.save(commit=False)
      obj.user = self.request.user
      obj.save()
      return HttpResponseRedirect(reverse('article:list'))


class Update(LoginRequiredMixin, UpdateView):
  model = Article
  fields = ['title', 'body', 'category']
  template_name = "diary/update.html"

  def get_object(self):
    slug_ = self.kwargs.get("slug")
    return get_object_or_404(Article, slug=slug_)

class Delete(LoginRequiredMixin, DeleteView):
  model = Article
  template_name = 'diary/delete.html'
  success_url = reverse_lazy('article:list')

  def get_object(self):
    slug_ = self.kwargs.get("slug")
    return get_object_or_404(Article, slug=slug_)


class LearnMore(TemplateView):
  template_name = 'diary/learn_more.html'