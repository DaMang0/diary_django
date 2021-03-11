from django.urls import include, path
from . import views
from .views import ArticleListView, ArticleCreate, ArticleDetail, ArticleDelete, ArticleUpdate, ArticleIndex, Test, Creativity_ArticleList


app_name = 'article'

urlpatterns = [
  # path('', views.home),
  path('article/list/', ArticleListView.as_view(), name='list'),

  path('article/creativity/list/', Creativity_ArticleList, name='creativity'),

  path('article/<slug:slug>/update/', ArticleUpdate.as_view(), name='update'),

  path('article/<slug:slug>/detail/', ArticleDetail.as_view(), name='detail'),

  path('article/create/', ArticleCreate.as_view(), name='create'),

  path('article/<slug:slug>/delete/', ArticleDelete.as_view(), name='delete'),

  path('article/test/', Test.as_view(), name='test'),

  path('', ArticleIndex.as_view(), name='index'),
  
  
  
]