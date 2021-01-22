from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, CreateView
from .models import Topic, Category
# Create your views here.
class ValueIndex(ListView):
  context_object_name = 'category'
  template_name = 'value/index.html'
  model = Category



class ValueTopicListView(ListView):
  model = Topic
  template_name = 'value/listView.html'

  def get_queryset(self):
    category = get_object_or_404(Category, name=self.kwargs.get('category'))
    return category.related_topic.all()
    # return Topic.objects.all().filter(category=t_category)


class CategoryCreateView(CreateView):
  model = Category
  fields = ['name']
  template_name = 'value/category_createForm.html'

  def __str__(self):
    return self.name
