from django.urls import include, path
from . import views
from .views import List, Create, Detail, Update, Delete, Index, LearnMore


app_name = 'article'

urlpatterns = [
  
  path('', Index.as_view(), name='index'),
  path('article/list/', List.as_view(), name='list'),

  path('article/learn-more/', LearnMore.as_view(), name='learn-more'), 
  

  # CRUD
  path('article/create/', Create.as_view(), name='create'),
  path('article/<slug:slug>/detail/', Detail.as_view(), name='detail'),
  path('article/<slug:slug>/update/', Update.as_view(), name='update'),
  path('article/<slug:slug>/delete/', Delete.as_view(), name='delete'),

  

  
  
  
  
]